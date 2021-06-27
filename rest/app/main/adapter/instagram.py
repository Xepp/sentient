import hashlib
import string
import random
from instagram_web_api import Client
from igramscraper.instagram import Instagram


class InstagramWebClient(Client):

    @staticmethod
    def _extract_rhx_gis(html):
        options = string.ascii_lowercase + string.digits
        text = ''.join([random.choice(options) for _ in range(8)])

        return hashlib.md5(text.encode()).hexdigest()


class InstagramWebAdapter:

    def __init__(self):
        self.api = InstagramWebClient(
            auto_patch=False,
            drop_incompat_keys=False,
            username='alirezakk22',
            password='waKM7T47Tf5nHYE'
        )

    def get_media_comments(self, shortcode, end_cursor=None, count=50):
        items = list()
        feed = self.api.media_comments(
            short_code=shortcode,
            end_cursor=end_cursor,
            count=count,
            extract=False
        )

        if not feed.get('status') == 'ok':
            raise Exception('status not ok!')

        result = feed.get('data', {}).get('shortcode_media', {}).get('edge_media_to_comment', {})
        new_end_cursor = result.get('page_info', {}).get('end_cursor')
        has_next_page = result.get('page_info', {}).get('has_next_page', False)
        edges = result.get('edges', [])
        edges = [edge.get('node') for edge in edges]
        items.extend(reversed(edges))

        return items, new_end_cursor, has_next_page


class InstagramScraperAdapter:

    def __init__(self):
        self.api = Instagram()
        #  self.api.with_credentials('alirezakk22', 'waKM7T47Tf5nHYE')
        #  self.api.login()

    @staticmethod
    def parse_comment(comment):
        return {
            'id': comment.identifier,
            'text': comment.text,
            'created_at': comment.created_at,
            'username': comment.owner.username
        }

    def get_media_comments(self, shortcode, end_cursor=None, count=200):
        items = self.api.get_media_comments_by_code(code=shortcode, count=count, max_id=end_cursor)

        comments = items['comments']
        new_end_cursor = items['next_page']
        has_next_page = True if new_end_cursor else False

        comments = [self.parse_comment(cm) for cm in comments]

        return comments, new_end_cursor, has_next_page

