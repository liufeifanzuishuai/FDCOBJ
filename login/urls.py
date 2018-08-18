#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.doLogin),
    url(r'^fist/$',views.fist_view),
    url(r'^fist/top.html/$',views.top_view),
    url(r'^fist/left.html/$',views.left_view),
    url(r'^fist/center.html/$',views.center_view),
    url(r'^fist/down.html/$',views.down_view),
]