#coding=utf-8
from django.conf.urls import url
from login import views
urlpatterns=[
    url(r'^$',views.doLogin),
    url(r'^first/$',views.showMain),
    url(r'^first/top.html/$', views.top_view),
    url(r'^first/left.html/$', views.left_view),
    url(r'^first/center.html/$', views.center_view),
    url(r'^first/down.html/$', views.down_view),
]