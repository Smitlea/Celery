from flask_testing import TestCase

from app import app


class BaseTestCase(TestCase):

    def create_app(self):
        # 必要。須回傳 Flask 實體。
        app.config['TESTING'] = True
        return app
