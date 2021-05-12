from __future__ import absolute_import, unicode_literals

import os

from celery import Celery, shared_task

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('recuritment')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# this is important to load the celery tasks
from celery.schedules import crontab
from recuritment.tasks import add

# 在代码里注册定时任务
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'recuritment.tasks.add',
        'schedule': 10.0,
        'args': (16, 4,)
    },
}


@app.on_after_configure.connect  # 系统启动完之后，开始任务
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='hello every 10')  # 调用test.s方法

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


# # 系统启用后，动态添加定时任务
# import json
# from django_celery_beat.models import PeriodicTask, IntervalSchedule
#
# # 先创建定时策略
# schdule, created = IntervalSchedule.objects.get_or_create(every=10, period=IntervalSchedule.SECONDS)
#
# # 在创建任务
# task = PeriodicTask.objects.create(interval=schdule, name="say hello 2025", task='recuritment.celery.test',
#                                    args=(json.dumps(["welcome"]),))


@app.task
def test(arg):
    print(arg)

app.conf.timezone = "Asia/Shanghai"

