#coding=utf-8
from django.conf.urls import url
from employee import views

urlpatterns = [
    url(r'^employinfo/$', views.Employinfo.as_view()),
    url(r'^edit$', views.Edit.as_view()),
    url(r'^detail$', views.detail),
    url(r'^delete$', views.delete),
    url(r'^houseinfo$', views.Houseinfo.as_view()),
    url(r'^house/add$', views.Houseadd.as_view()),
    url(r'^house/edit$', views.Houseedit.as_view()),
    url(r'^house/delete$', views.housedelete),
    url(r'^housetypeinfo$', views.Housetypeinfo.as_view()),
    url(r'^housetype/add$', views.Housetypeadd.as_view()),
    url(r'^housetype/delete$', views.housetypedelete),
    url(r'^department$', views.Department.as_view()),
    url(r'^department/delete$', views.departmentdelete),
    url(r'^notice$', views.Notices.as_view()),
    url(r'^notice/add$', views.Noticesadd.as_view()),
    url(r'^notice/delete$', views.noticedelete),
]



