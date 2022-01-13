import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'project.settings.prod')

app = Celery('project')

app.config_from_object('django.conf:settings', namespace='CELERY')


@app.on_after_finalize.connect
def setup_periodic_task(sender, **kwargs):
    pass


app.autodiscover_tasks()
