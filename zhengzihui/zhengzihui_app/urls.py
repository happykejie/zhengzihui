from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^service_detail/$', views.service_detail, name='service_detail'),
]