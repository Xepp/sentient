import io
import os
import json
import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Bidirectional
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import SpatialDropout1D
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from preprocess import text_cleaner
from preprocess import word_tokenizer


class BaseModel(object):
    ASSETS_DIR = 'assets'

    def train(self, X_train, Y_train):
        raise NotImplementedError

    def analyze(self, X_test, Y_test):
        raise NotImplementedError

    def predict(self, texts):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

    def load_or_train(self, X_train, Y_train, X_test, Y_test):
        try:
            self.load()
        except Exception:
            self.train(X_train, Y_train)
            self.analyze(X_test, Y_test)


class LinearSVCModel(BaseModel):
    def __init__(self):
        self.model = Pipeline([
            ('vect', CountVectorizer(tokenizer=word_tokenizer, analyzer='word', ngram_range=(1, 3), min_df=1,
                lowercase=False)),
            ('tfidf', TfidfTransformer(sublinear_tf=True)),
            ('clf-svm', LinearSVC(loss='hinge', penalty='l2', max_iter=100))
        ])

    def train(self, X_train, Y_train):
        self.model = self.model.fit(X_train, Y_train)

        # Save
        os.makedirs(os.path.dirname(f'{self.ASSETS_DIR}/svc.joblib'), exist_ok=True)
        joblib.dump(self.model, f'{self.ASSETS_DIR}/svc.joblib') 

    def analyze(self, X_test, Y_test):
        print(f'{self.__class__.__name__} Accuracy: {self.model.score(X_test, Y_test)}')

    def predict(self, texts):
        texts = [text_cleaner(text) for text in texts]

        return self.model.predict(texts)

    def load(self):
        self.model = joblib.load(f'{self.ASSETS_DIR}/svc.joblib')


class BiLSTMModel(BaseModel):
    def __init__(self):
        self.vocab_size = 2000
        self.encoder = TextVectorization(
            max_tokens=self.vocab_size)
        self.le = LabelEncoder()
        self.le.fit_transform(['neu', 'neg', 'pos'])

    def train(self, X_train, Y_train):
        Y_train = to_categorical(self.le.transform(Y_train), 3)
        self.encoder.adapt(X_train)
        self.model = Sequential([
            self.encoder,
            Embedding(
                input_dim=len(self.encoder.get_vocabulary()),
                output_dim=64,
                mask_zero=True),
            Bidirectional(LSTM(64, return_sequences=True)),
            Bidirectional(LSTM(32)),
            Dense(64, activation='relu'),
            Dropout(0.5),
            Dense(3, activation='softmax')])
        self.model.compile(
            loss=CategoricalCrossentropy(),
            optimizer=Adam(1e-4),
            metrics=['accuracy'])
        self.model.fit(
            x=X_train,
            y=Y_train,
            epochs=10)

    def analyze(self, X_test, Y_test):
        self.model.summary()
        Y_test = to_categorical(self.le.transform(Y_test), 3)
        test_loss, test_acc = self.model.evaluate(x=X_test,
                                                  y=Y_test)

        print(f'{self.__class__.__name__} Accuracy: {test_acc} Loss: {test_loss}')

    def predict(self, texts):
        texts = [text_cleaner(text) for text in texts]
        p = self.model.predict(texts)
        y_classes = [np.argmax(y, axis=None, out=None) for y in p]

        return self.le.inverse_transform(y_classes)


class SparseModel(BaseModel):
    def __init__(self):
        self.embedding_dimension = 64
        self.vocab_size = 2000
        self.max_length = 100
        self.oov_tok = '<OOV>'
        self.truncate_type = 'post'
        self.padding_type = 'post'
        self.tokenizer = Tokenizer(
            num_words=self.vocab_size,
            oov_token=self.oov_tok)
        self.le = LabelEncoder()
        self.le.fit_transform(['neu', 'neg', 'pos'])

    def train(self, X_train, Y_train):
        Y_train = self.le.transform(Y_train)
        self.tokenizer.fit_on_texts(X_train)
        X_train = self.tokenizer.texts_to_sequences(X_train)
        word_index = self.tokenizer.word_index
        X_train = pad_sequences(
            X_train,
            maxlen=self.max_length,
            padding=self.padding_type,
            truncating=self.truncate_type)
        self.model = Sequential([
            Embedding(
                input_dim=len(word_index)+1,
                output_dim=self.embedding_dimension),
            SpatialDropout1D(0.3),
            Bidirectional(LSTM(self.embedding_dimension, dropout=0.3, recurrent_dropout=0.3)),
            Dense(self.embedding_dimension, activation='relu'),
            Dropout(0.8),
            Dense(3, activation='softmax')])
        self.model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])
        self.history = self.model.fit(
            x=X_train,
            y=Y_train,
            epochs=8)
        
        # Save
        self.model.save(f'{self.ASSETS_DIR}/sparse.model')
        tokenizer_json = self.tokenizer.to_json()
        with io.open(f'{self.ASSETS_DIR}/sparse.tokenizer.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(tokenizer_json, ensure_ascii=False))

    def analyze(self, X_test, Y_test):
        self.model.summary()
        Y_test = self.le.transform(Y_test)
        X_test = self.tokenizer.texts_to_sequences(X_test)
        X_test = pad_sequences(
            X_test,
            maxlen=self.max_length,
            padding=self.padding_type,
            truncating=self.truncate_type)
        test_loss, test_acc = self.model.evaluate(
            x=X_test,
            y=Y_test)

        print(f'{self.__class__.__name__} Accuracy: {test_acc} Loss: {test_loss}')

    def predict(self, texts):
        texts = [text_cleaner(text) for text in texts]
        texts = self.tokenizer.texts_to_sequences(texts)
        texts = pad_sequences(
            texts,
            maxlen=self.max_length,
            padding=self.padding_type,
            truncating=self.truncate_type)
        p = self.model.predict(texts)
        y_classes = [np.argmax(y, axis=None, out=None) for y in p]

        return self.le.inverse_transform(y_classes)

    def load(self):
        self.model = load_model(f'{self.ASSETS_DIR}/sparse.model')
        with open(f'{self.ASSETS_DIR}/sparse.tokenizer.json') as f:
            data = json.load(f)
            self.tokenizer = tokenizer_from_json(data)
