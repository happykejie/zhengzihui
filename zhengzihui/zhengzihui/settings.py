#coding:utf-8

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

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)'''


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
    'fr_app',
    'zhengzihui_app',
    #'django.contrib.admin.apps.SimpleAdminConfig',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
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

         'PASSWORD':'123456',#password of mysql user

	 'HOST':'127.0.0.1',#localhost
	 'PORT':'3306',#defaut port of mysql
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

#YZ change for admin cn
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

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
     'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
     },
    #'MENU_OPEN_FIRST_CHILD': False, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
     'MENU': (
         'sites',
        #{'app': 'zhengzihui_app', 'label': u'站点内容管理'},  
        {'app': 'auth','label':u'认证系统', 'icon':'icon-lock', 'models': ('user', 'group')},
        {'label': u'关于用户','models': ('zhengzihui_app.tb_user', 'zhengzihui_app.tb_user_expand')},
        {'label': u'关于新闻和公告','models': ('zhengzihui_app.tb_pic', 'zhengzihui_app.tb_album','zhengzihui_app.tb_area','zhengzihui_app.tb_article','zhengzihui_app.tb_accessory')},
        {'label': u'关于服务信息','models': ('zhengzihui_app.tb_goods', 'zhengzihui_app.tb_goods_class','zhengzihui_app.tb_goods_click','label','zhengzihui_app.tb_goods_evaluation','zhengzihui_app.tb_service_provider')},
        {'label': u'附件相关','models': ('zhengzihui_app.tb_pic', 'zhengzihui_app.tb_album','zhengzihui_app.tb_area','zhengzihui_app.tb_article','zhengzihui_app.tb_accessory')},
        {'label': u'关于站内消息','models': ('zhengzihui_app.tb_Message', 'zhengzihui_app.tb_MessageText','zhengzihui_app.tb_SysMessage')},
        {'label': u'关于订单','models': ('zhengzihui_app.tb_order', 'zhengzihui_app.tb_Artificial_Representations')},
        {'label': u'关于项目','models': ('zhengzihui_app.tb_item', 'zhengzihui_app.tb_item_class','zhengzihui_app.tb_item_click','zhengzihui_app.tb_item_pa')},
        #{'model':'zhengzihui_app.tb_user','label':u'用户','icon':'icon-user'}, 
        {'app':'zhengzihui_app','label': u'所有站点内容管理', 'models': (
            

            {'model': 'zhengzihui_app.tb_user', 'label': u'用户'},#中文化左侧管理表的代码
            {'model': 'zhengzihui_app.tb_user_expand','label': u'用户扩展信息'},
            

            {'model': 'zhengzihui_app.tb_pic','label': u'图片表'},
            {'model': 'zhengzihui_app.tb_album','label': u'相册表'},
            {'model': 'zhengzihui_app.tb_area','label': u'地区表'},
            {'model': 'zhengzihui_app.tb_article','label': u'文章表'},
            {'model': 'zhengzihui_app.tb_accessory','label': u'其他附件表'},
            
            
            {'model': 'zhengzihui_app.Tb_Apage','label': u'单页表'},
            {'model': 'zhengzihui_app.Tb_Apage_Class','label': u'单页分类表'},
            {'model': 'zhengzihui_app.tb_News_Class','label': u'新闻分类'},
            {'model': 'zhengzihui_app.tb_News','label': u'新闻'},
            {'model': 'zhengzihui_app.Tb_Notice','label': u'公告'},
            {'model': 'zhengzihui_app.Tb_Notice_Class','label': u'公告分类表'},
            
            {'model': 'zhengzihui_app.tb_goods','label': u'服务信息表'},
            {'model': 'zhengzihui_app.tb_goods_class','label': u'服务分类表'},
            {'model': 'zhengzihui_app.tb_goods_click','label': u'服务点击表'},
            {'model': 'zhengzihui_app.tb_goods_evaluation','label': u'服务评价表'},
            {'model': 'zhengzihui_app.tb_service_provider','label': u'服务提供商'},
            
         
            
            {'model': 'zhengzihui_app.tb_Message','label': u'站内短信表'},
            {'model': 'zhengzihui_app.tb_MessageText','label': u'站内短信内容表'},
            {'model': 'zhengzihui_app.tb_SysMessage','label': u'系统信息表'},
            
            {'model': 'zhengzihui_app.tb_item','label': u'项目详情表'},
            {'model': 'zhengzihui_app.tb_item_class','label': u'项目分类表'},
            {'model': 'zhengzihui_app.tb_item_click','label': u'项目点击表'},
            {'model': 'zhengzihui_app.tb_item_pa','label': u'项目发布机构表'},
            
            {'model': 'zhengzihui_app.tb_order','label': u'订单表'},
            {'model': 'zhengzihui_app.tb_Artificial_Representations','label': u'人工申诉表'},
            
            #等待完成中
        )},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
     ),

    # misc
     'LIST_PER_PAGE': 10 #分页，显示项目的条数应该有多少
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

#email config
EMAIL_HOST='smtp.qq.com'
EMAIL_HOST_USER='changyifan123@qq.com'
EMAIL_HOST_PASSWORD='yxvourocuizwbjbh'
EMAIL_USE_TLS = True
#SESSION浏览器关闭后失效
SESSION_EXPIRE_AT_BROWSER_CLOSE=True 
