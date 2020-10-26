from hazm import Normalizer
from hazm import Lemmatizer
from hazm import word_tokenize


PUNCS = ['،', '.', ',', ':', ';', '"']
NORMALIZER = Normalizer()
LEMMATIZER = Lemmatizer()

def text_cleaner(text):
    normalized = NORMALIZER.normalize(text)
    tokenized = word_tokenizer(normalized)
    tokens = []
    for t in tokenized:
        temp = t
        for p in PUNCS:
            temp = temp.replace(p, '')
        tokens.append(temp)
    tokens = [w for w in tokens if not len(w) <= 1]
    tokens = [w for w in tokens if not w.isdigit()]
    tokens = [LEMMATIZER.lemmatize(w) for w in tokens]

    return ' '.join(tokens)


def word_tokenizer(text):
    return word_tokenize(text)

