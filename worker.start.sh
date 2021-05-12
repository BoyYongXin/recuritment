# 启动 recruitment 这个 package 的时候，会运行 __init__.py
# __init__.py 里面初始化了 django 的配置
#DJANGO_SETTINGS_MODULE=settings.production celery -A recruitment worker -l INFO
DJANGO_SETTINGS_MODULE=settings.local celery -A recuritment worker -l INFO

# 启动flower监控服务
#DJANGO_SETTINGS_MODULE=settings.local celery -A recuritment flower --broker=redis://127.0.0.1/0
#DJANGO_SETTINGS_MODULE=settings.local celery -A recuritment flower

