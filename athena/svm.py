import numpy as np

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

from dataset import get_dataset
from preprocess import text_cleaner
from preprocess import word_tokenizer 


##### Dataset #####
x_train, y_train, x_test, y_test = get_dataset(test_size=0.25)


##### PreProcess #####
x_train = x_train.map(text_cleaner)
x_test  = x_test.map(text_cleaner)

x_train = np.asarray(x_train)
y_train = np.asarray(y_train)
x_test  = np.asarray(x_test)
y_test  = np.asarray(y_test)


##### SVM #####
svm = Pipeline([
          ('vect', CountVectorizer(tokenizer=word_tokenizer, analyzer='word', ngram_range=(1, 2), min_df=1, lowercase=False)),
          ('tfidf', TfidfTransformer(sublinear_tf=True)),
          ('clf-svm', LinearSVC(loss='hinge', penalty='l2', max_iter=10))
      ])

svm = svm.fit(x_train, y_train)
print('Linear SVC Model Score: ', svm.score(x_test, y_test))

