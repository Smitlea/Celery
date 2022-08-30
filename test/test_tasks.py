from tasks import add_celery, count
from . import BaseTestCase


class Test_tasks(BaseTestCase):
    def test_run(self):
        self.tasks = count.apply({'x': 3})
        self.assertEqual(self.tasks.state, "SUCCESS")

    def test_add_celery(self):
        res = add_celery.apply({'x': 5}, {'y': 5})
        self.assertEqual(res.state, "SUCCESS")
