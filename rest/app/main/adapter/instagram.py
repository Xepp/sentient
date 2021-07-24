import hashlib
import string
import random
import json
from instagram_web_api import Client
from igramscraper.instagram import Instagram
from instagram_scraper import InstagramScraper
from instagram_scraper.constants import QUERY_COMMENTS, QUERY_COMMENTS_VARS


class InstagramScraperClient(InstagramScraper):
    def get_comments_by_shortcode(self, shortcode, end_cursor=''):
        params = QUERY_COMMENTS_VARS.format(shortcode, end_cursor)
        self.update_ig_gis_header(params)

        resp = self.get_json(QUERY_COMMENTS.format(params))

        if resp is not None:
            payload = json.loads(resp)['data']['shortcode_media']

            if payload:
                container = payload['edge_media_to_comment']
                comments = [node['node'] for node in container['edges']]
                end_cursor = container['page_info']['end_cursor']
                has_next_page = container['page_info']['has_next_page']

                return comments, end_cursor, has_next_page

        return [], None, False


class CustomInstagramScraper:
    def __init__(self):
        self.api = InstagramScraperClient(
            login_user='alirezakk22',
            login_pass='waKM7T47Tf5nHYE'
        )
        self.api.authenticate_with_login()

    @staticmethod
    def parse_comment(comment):
        return {
            'id': comment.get('id'),
            'text': comment.get('text'),
            'created_at': comment.get('created_at'),
            'username': comment.get('owner', {}).get('username')
        }

    def get_media_comments(self, shortcode, end_cursor=None):
        if end_cursor is None:
            end_cursor = ''
        items, new_end_cursor, has_next_page = self.api.get_comments_by_shortcode(shortcode=shortcode, end_cursor=end_cursor)

        comments = [self.parse_comment(cm) for cm in items]

        return comments, new_end_cursor, has_next_page


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
        self.api.user_agent = 'Mozilla/5.0 (Linux; Android 10; SM-N975U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.89 Mobile Safari/537.36 Instagram 135.0.0.28.119 Android (29/10; 480dpi; 1080x2051; samsung; SM-N975U; d2q; qcom; en_US; 206670927)'

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
