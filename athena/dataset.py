import os
import pandas as pd
from sklearn.model_selection import train_test_split


def get_dataset(file_path_list=None, test_size=0.2):
    if file_path_list is None:
        file_path_list = os.listdir('dataset')

    all_files = [fname for fname in os.listdir('dataset')]
    files = [f'dataset/{fname}' for fname in all_files if fname in file_path_list]
    dataframes = list()
    for f in files:
        dataframes.append(pd.read_csv(f, index_col=None, header=0, encoding='utf-8'))

    df = pd.concat(dataframes, axis=0, ignore_index=True)
    df = df[df.sentiment.ne('unk')]
    df = df.filter(items=['content', 'sentiment'])
    df.dropna(inplace=True)

    train, test = train_test_split(df, test_size=0.2)

    x_train = train.pop('content')
    y_train = train.pop('sentiment')
    x_test = test.pop('content')
    y_test = test.pop('sentiment')

    return x_train, y_train, x_test, y_test


if __name__ == '__main__':
    from collections import Counter

    x_train, y_train, x_test, y_test = get_dataset()

    print('Train distribution: ', dict(Counter(y_train)))
    print('Test  distribution: ', dict(Counter(y_test)))
