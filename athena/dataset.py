import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split


def get_dataset(file_path='dataset.csv', test_size=0.2):
    dataset = pd.read_csv(file_path, encoding='utf-8')
    dataset = dataset[dataset.sentiment.ne('unk')]
    dataset = dataset.filter(items=['content', 'sentiment'])
    dataset.dropna(inplace=True)

    train, test = train_test_split(dataset, test_size=test_size)

    x_train = train.pop('content')
    y_train = train.pop('sentiment')

    x_test = test.pop('content')
    y_test = test.pop('sentiment')

    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    x_train, y_train, x_test, y_test = get_dataset(file_path='tagged.csv')

    from collections import Counter

    print('Train distribution: ', dict(Counter(y_train)))
    print('Test  distribution: ', dict(Counter(y_test)))

