import os
from celery import Celery, Task
import time


CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL', 'redis://localhost:6379/0')

Celery_app = Celery(
    __name__,
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL
)


class MyCelery(Task):
    def run(self, x: int, y: int):

        for x in range(20):
            x = x+y
            self.update_state(state='PROGRESS', meta={'current': (x+y)})
            print(x+y)
            time.sleep(1)
        return {'status': 'SUCCESS'}


add_celery = Celery_app.register_task(MyCelery())


@Celery_app.task(bind=True)
def count(self, x: int):

    for x in range(20):

        self.update_state(status='PROGRESS', meta={'currency': x, "total": 20})
        time.sleep(1)

        return {'status': 'complete'}


#Celery_register = Celery_app.register_task(MyCelery())

# Register a task in the task registry.
# The task will be automatically instantiated if not already an instance. Name must be configured prior to registration.
