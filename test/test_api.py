
import json
from . import BaseTestCase


class TestAccountApi(BaseTestCase):
    def test_register(self):  # 測試網頁
        # 實際送出請求
        response = self.client.post(
            '/register',
            data=json.dumps({
                'recipient': 'allen@yahoo.com',
                'title': 'Its_been_test',
                'content': 'whats do we have here'
            }),
            content_type='application/json'
        )

        self.assertEqual(
            response.json, {'status': 0, 'message': 'success', 'task_id': 'task_id'})
        self.assertEqual(response.status_code, 200)

    def test_register_error(self):  # 測試錯誤

        response = self.client.post(
            '/register',
            data=json.dumps({}),
            content_type='application/json'
        )

        self.assertEqual(
            response.json, {'status': 1, 'message': 'error', 'task_id': 'task_id'})
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = self.client.get(
            '/get',
            data=json.dumps({
                'id': "123"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)


# # pipenv run celery -A tasks.Celery_app worker --pool=solo -l info
