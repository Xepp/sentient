from app.main.adapter.instagram import InstagramWebAdapter


class InstagramService:

    def __init__(self):
        self.adapter = InstagramWebAdapter()

    def get_comments(self, shortcode, end_cursor=None):
        comments, new_end_cursor, has_next_page = self.adapter.get_media_comments(shortcode=shortcode, end_cursor=end_cursor)

        return comments, new_end_cursor, has_next_page

