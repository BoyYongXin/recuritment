"""
Django settings for recuritment project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import platform
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7m7engi&*m6q148)%$*canj#rz3)ckq86d@yf+cq-q086f@*gq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost","127.0.0.1"]

LOGIN_REDIRECT_URL = '/'   # 登录后呈现给用户的页面
LOGIN_URL = '/accounts/login/'

# Application definition

INSTALLED_APPS = [
    'grappelli',
    'bootstrap4', # Bootstrap 来定制页面样式
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'running',
    'jobs',
    'interview',
    'django_python3_ldap',
    'rest_framework',
    'django_celery_beat',
    #'django_oss_storage', 启用oss服务
    'recuritment.apps.UniversalManagerApp',#自动注册model
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'interview.performance.PerformanceAndExceptionLoggerMiddleware',# 日志中间件。类实现
    # 'interview.performance.performance_logger_middleware',# 日志中间件 ，函数
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',#配置多语言的中间件

    'django.middleware.cache.UpdateCacheMiddleware', # 更新缓存的数据
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',#优先从缓存系统取数据
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recuritment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'recuritment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # 'running': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'running',
    #     'USER': 'recruitment',
    #     'PASSWORD': 'recruitment',
    #     'HOST': 'running',
    #     'PORT': '3306',
    # },
}
# 数据库路由，可以用来做读写分离
# DATABASE_ROUTERS = ['settings.router.DatabaseRouter']

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGES = [
    ('zh-hans', _('Chinese')),
    ('en', _('English')),
]
LANGUAGE_CODE = 'zh-hans'#'en-us'

TIME_ZONE = 'Asia/Shanghai'#'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
LOG_DIR = "/data/logs/recruitment/"

# STATIC_ROOT = 'static'

# 存储图片路径
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


if platform.system() == "Linux" or platform.system() == "Windows":
    # linux or windows
    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
elif platform.system() == "Darwin" or platform.system() == "Mac":
    # OS X,
    # you could not create a folder at /data/logs dure to OS default policy
    LOG_DIR = BASE_DIR


# redis cache is disabled, change "CACHES_redis" to "CACHES" to enable it

# 加入redis的缓存
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        'TIMEOUT': 60, # default expire time per api call
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "mysecret",
            "SOCKET_CONNECT_TIMEOUT": 5,  # in seconds
            "SOCKET_TIMEOUT": 5,  # r/w timeout in seconds
            # 'MAX_ENTRIES': 10000,
            # 'KEY_PREFIX': 'recruit-',
        }
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': { # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },

        'mail_admins': { # Add Handler for mail_admins for `warning` and above
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            #'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'recruitment.admin.log'),
        },

        'performance': {
            #'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(LOG_DIR, 'recruitment.performance.log'),
        },
    },

    # 'root': {
    #     'handlers': ['console', 'file'],
    #     'level': 'INFO',
    # },

    'loggers': {
        "django_python3_ldap": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
        },

    "interview.performance": {
        "handlers": ["console", "performance"],
        "level": "INFO",
        "propagate": False,
    },
    },
}

### LDAP
'''  
# The URL of the LDAP server.
LDAP_AUTH_URL = "ldap://localhost:389"
# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False

# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "dc=ihopeit,dc=com"

# The LDAP class that represents a user. # 哪些用户可以用来登陆的
LDAP_AUTH_OBJECT_CLASS = "inetOrgPerson"# 组织成员

# User model fields mapped to the LDAP
# attributes that represent them.
LDAP_AUTH_USER_FIELDS = {
    "username": "cn",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

# A tuple of django model fields used to uniquely identify a user.
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)

# Path to a callable that takes a dict of {model_field_name: value},
# returning a dict of clean model data.
# Use this to customize how data loaded from LDAP is saved to the User model.
LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"

# The LDAP username and password of a user for querying the LDAP database for user
# details. If None, then the authenticated user will be used for querying, and
# the `ldap_sync_users` command will perform an anonymous query.
LDAP_AUTH_CONNECTION_USERNAME = None
LDAP_AUTH_CONNECTION_PASSWORD = None

# 可以使用 ldap 的等方式来登陆我们的系统   "django_python3_ldap.auth.LDAPBackend"
# djano 自带的登录方式来登陆我们的系统     django.contrib.auth.backends.ModelBackend
AUTHENTICATION_BACKENDS = {"django_python3_ldap.auth.LDAPBackend",'django.contrib.auth.backends.ModelBackend',}
'''
