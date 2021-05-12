import os
from .base import *

ALLOWED_HOSTS = ["127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = '7m7engi&*m6q148)%$*canj#rz3)ckq86d@yf+cq-q086f@*gq'

INSTALLED_APPS += (
    # other apps for production site
)


## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK_TOKEN = os.environ.get('DINGTALK_WEB_HOOK_TOKEN','')
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=%s" % DINGTALK_WEB_HOOK_TOKEN


## celery  基础配置
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYD_MAX_TASKS_PER_CHILD = 10
CELERYD_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_work.log")
CELERYBEAT_LOG_FILE = os.path.join(BASE_DIR, "logs", "celery_beat.log")


###########################
STATIC_URL = 'http://icdn.ihopeit.com/static/'
#STATIC_URL = '/static/'

# 阿里云 CDN 存储静态资源文件 & 阿里云存储上传的图片/文件
# STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
OSS_ACCESS_KEY_ID = os.environ.get('OSS_ACCESS_KEY_ID','')
# AliCloud access key secret
OSS_ACCESS_KEY_SECRET = os.environ.get('OSS_ACCESS_KEY_SECRET','')
# The name of the bucket to store files in
OSS_BUCKET_NAME = 'djangorecruit'

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-beijing.aliyuncs.com'
##########################