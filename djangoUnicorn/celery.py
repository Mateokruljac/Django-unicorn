import os

from celery import Celery

# set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoUnicorn.settings.local')

# app = Celery('djangoUnicorn',
#              broker_use_ssl={
#                  'ssl_cert_reqs': ssl.CERT_NONE
#              },
#              redis_backend_use_ssl={
#                  'ssl_cert_reqs': ssl.CERT_NONE
#              }
#              )

app = Celery('djangoUnicorn')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
