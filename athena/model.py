from preprocess import text_cleaner
from svm import svm


class Model:

    def predict(self, text_list):
        clean_text_list = [text_cleaner(text) for text in text_list]
        return svm.predict(clean_text_list)


if __name__ == '__main__':
    model = Model()
    print(model.predict(['سلام چطوری', 'خیلی خوبه']))

