# celery.py
import os
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@worker_ready.connect
def at_start(sender, **kwargs):
    print('Celery worker is ready!')

app.conf.update(
    worker_send_task_events=True,
    task_serializer='json',
    accept_content=['json'],
    broker_connection_retry_on_startup=True,  # Add this line
)