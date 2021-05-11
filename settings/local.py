from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = '7m7engi&*m6q148)%$*canj#rz3)ckq86d@yf+cq-q086f@*gq'

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
# LDAP_AUTH_URL = "ldap://192.168.31.250:389"
# LDAP_AUTH_CONNECTION_USERNAME = "admin"
# LDAP_AUTH_CONNECTION_PASSWORD = "admin_passwd_4_ldap"

INSTALLED_APPS += (
    # other apps for production site
)


## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=xxxxx"

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


###  设置sentry 错误日志收集

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

'''
sentry_sdk.init(
    dsn="http://xxx@recruit.ihopeit.com:9000/2",
    integrations=[DjangoIntegration()],
    # performance tracing sample rate, 采样率, 生产环境访问量过大时，建议调小（不用每一个URL请求都记录性能）
    traces_sample_rate=1.0, # 

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)
'''