
import json
from unittest.mock import patch
from urllib import request
from webbrowser import get
from tasks import add_celery, count
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

    # @patch{'app.request.value.get'}
    # def test_result(self):  # 測試結果
    #     response = self.client.get(
    #         '/result',
    #         data=json.dumps({
    #             'task_id': "123"

    #         }),
    #         content_type='application/json'
    #     )

    #     self.assertEqual(response.status_code, 200)


# class TestCeleryTask(BaseTestCase):
#     def test_tasks(self):  # 測試tasks
#         response = self.client.get(
#             '/add',
#             data=json.dumps({
#                 'id': "123"
#             }),


#             content_type='application/json'
#         )

#         response = AsyncResult(response)
#         # task = add_celery(),
#         # self.assertEqual(task),
#         self.assertEqual(response.status_code, 200)
# # pipenv run celery -A tasks.Celery_app worker --pool=solo -l info
