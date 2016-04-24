﻿#coding:utf-8

"""
Django settings for zhengzihui project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)



import os
#YZ addfor suit
'''
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+a^0qwojpxsam*xa5*y_5o+#9fej#+w72m998sjc!e)oj9im*y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #YZ addfor suit
    'suit',
    #YZ addfor filer
    'easy_thumbnails',
    #'filer',暂时用不到
    'mptt',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'zhengzihui_app',
    #'django.contrib.admin.apps.SimpleAdminConfig',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'zhengzihui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],#YZ change for admin templates
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

WSGI_APPLICATION = 'zhengzihui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#YZ use mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
      #there have a option
	 'NAME':'zhengzihui_test_second',#your database name
	 'USER':'root',#your username of mysql
	 'PASSWORD':'123654',#password of mysql user
	 'HOST':'127.0.0.1',#localhost
	 'PORT':'3306',#defaut port of mysql
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#YZ change for admin cn
LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

#YZ for collectstatic
STATIC_ROOT = 'C:/ZHENGZIHUI/zhengzihui/static/'


#YZ add Image
MEDIA_ROOT = 'zhengzihui_app/static/zhengzihui_app/'

MEDIA_URL = 'zhengzihui_app/static/zhengzihui_app/'




#YZ config of suit

SUIT_CONFIG = {
    #header
     'ADMIN_NAME':'政资汇后台管理系统',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
     'MENU': (
         'sites',
        {'app': 'zhengzihui_app', 'label': u'站点内容管理'},  
         {'app': 'auth','label':u'认证系统', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
     ),

    # misc
    # 'LIST_PER_PAGE': 15
}

#YZ add for filer Thumbnails :For easy_thumbnails to support retina displays (recent MacBooks, iOS) add to settings.py:
THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
