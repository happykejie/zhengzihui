#-*- coding:utf-8 -*-

from django.conf.urls import include, url

urlpatterns = [
    url(r'frame/','fr_app.views.frame',name='frame'),
    url(r'verification/','fr_app.views.verification'
        ,name='verification'),
    url(r'require_finish','fr_app.views.require_finish',name='require_finish'),
]
