#coding=utf-8
from django.conf.urls import url

from customer import views

urlpatterns=[
    url(r'distribute/$',views.Distribute.as_view()),
    url(r'singledis/$',views.singledis)

]