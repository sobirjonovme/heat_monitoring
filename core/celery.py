import os
from pathlib import Path

import environ
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
BASE_DIR = Path(__file__).resolve().parent.parent

# READING ENV
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", env.str("DJANGO_SETTINGS_MODULE"))

app = Celery("core")

# Configure Celery to use Redis as the message broker
app.config_from_object("django.conf:settings", namespace="CELERY")
# app.conf.broker_url = "redis://localhost:6379/0"

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(packages=settings.INSTALLED_APPS)
