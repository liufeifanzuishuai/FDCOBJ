# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from db_manager.models import *
# Create your views here.
userNum=''#定义一个全局变量传给页面的‘您好：’
def doLogin(request):
    if request.method=="GET":
        #判断request中是否有名字是"login"的cookie--
         if request.COOKIES.has_key('login'):
             login = request.COOKIES['login']
             login_list = login.split(',')
             uname = login_list[0]
             upwd = login_list[1]
             return render(request,'login.html',{'uname':uname,"upwd":upwd}) #如果检查到有cookie就回返给页面。ok--
         return render(request,'login.html')#如果没有cookie那么就直接返回页面就行了--
    else:
        response=HttpResponse()
        global userNum
        userNum=request.POST.get('userNum')
        userPw=request.POST.get('userPw')
        flag=request.POST.get('flag')
        #需要从数据库获取用户名和密码,注意这里不需要判断非空。-
        s_count=Employee_Info.objects.filter(employee_account=userNum,employee_password=userPw).count()
        errori=True
        if s_count==1:
            response.content='登陆成功'
            #这里需要给前端页面一个判断如果密码失败就alter--
            errori=False
            if flag:
                response.set_cookie('login',userNum+','+userPw,max_age=3*24*60*60,path='/login/')
            else:
                #这里判断不勾选记住密码，那么一定要删除cookie--
                # response.delete_cookie('login')
                response.set_cookie('login',max_age=0,path='/login/')
            response.setdefault('Location', '/login/fist/')
            response.status_code = 302
            return response
        else:
            #这里是密码失败返回True给前端页面--
            errori=True
            response.content='登陆失败'
            #这时候就是登陆失败，登陆失败时候需要删除cookie--
            response.delete_cookie('login')
            #并且重定向到登陆界面--
            response.status_code=302
            response.setdefault('Location','/login/')
            return render(request,'login.html',{'errori':errori})

def fist_view(request):
    return render(request,'main.html')


def top_view(request):
    return render(request,'top.html')


def left_view(request):
    return render(request,'left.html')


def center_view(request):
    return render(request,'center.html')


def down_view(request):
    return render(request,'down.html')