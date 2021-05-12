#DJANGO_SETTINGS_MODULE=settings.production celery -A recuritment flower
DJANGO_SETTINGS_MODULE=settings.local celery -A recuritment flower
