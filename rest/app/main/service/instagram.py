#  from app.main.adapter.instagram import InstagramWebAdapter
#  from app.main.adapter.instagram import InstagramScraperAdapter
from app.main.adapter.instagram import CustomInstagramScraper


class InstagramService:

    def __init__(self):
        #  self.adapter = InstagramWebAdapter()
        #  self.adapter = InstagramScraperAdapter()
        self.adapter = CustomInstagramScraper()

    def get_comments(self, shortcode, end_cursor=None):
        comments, new_end_cursor, has_next_page = self.adapter.get_media_comments(shortcode=shortcode, end_cursor=end_cursor)

        return comments, new_end_cursor, has_next_page
