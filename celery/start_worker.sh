#celery -A tasks -Q toutiaoh worker --loglevel=info
celery -A tasks worker --loglevel=info
#celery -app tasks -Q toutiaoh worker --loglevel=info


# 任务监控web
#https://docs.celeryproject.org/en/master/userguide/monitoring.html#flower-real-time-celery-web-monitor
celery -A tasks flower --broker=redis://127.0.0.1/0
