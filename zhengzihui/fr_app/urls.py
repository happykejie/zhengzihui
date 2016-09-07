#-*- coding:utf-8 -*-

from django.conf.urls import include, url

urlpatterns = [
    #free require part（免费需求发布）
    url(r'^frame/','fr_app.views.frame',name='frame'),
    url(r'^verification/','fr_app.views.verification',name='verification'),
    url(r'^require_finish','fr_app.views.require_finish',name='require_finish'),
    #Supporting Center part (配套中心)（懒得再做一个独立的app了，所以就放到这里）
    url(r'^supporting_center/frame','fr_app.views.supporting_center_frame'
        ,name='supporting_center_frame'),
    url(r'^supporting_center/iteminfo','fr_app.views.supporting_center_iteminfo'
        ,name='supporting_center_iteminfo'),
    url(r'^supporting_center/filter_labels','fr_app.views.supporting_center_filter_labels'
        ,name='supporting_center_filter_labels'),
    url(r'^supporting_center/shoucang_item/','fr_app.views.supporting_center_shoucang_item'
        ,name="supporting_center_shoucang_item"),
]
