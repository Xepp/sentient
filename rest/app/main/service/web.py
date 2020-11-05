from app.main.adapter.web import KhabarFooriAdapter


class KhabarFooriService:

    def __init__(self):
        self.adapter = KhabarFooriAdapter()

    def get_comments(self, url):
        comments = self.adapter.get_page_comments(url=url)

        return comments

