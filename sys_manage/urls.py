#coding=utf-8
from django.conf.urls import url
import views

urlpatterns=[
    url(r'^employee/$', views.employee_view),
    url(r'^department/$', views.department_view),
    url(r'^role/$', views.role_view),
    url(r'^look_role/$', views.look_role_view),
]