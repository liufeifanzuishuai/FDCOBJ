# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import operator
import datetime
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
                response.set_cookie('login',userNum+','+userPw,max_age=3*24*60*60,path='/')
            else:
                #这里判断不勾选记住密码，那么一定要删除cookie--
                # response.delete_cookie('login')
                response.set_cookie('login',max_age=0,path='/')
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
    try:
        login = request.COOKIES['login']
    except:
        login = 'admin,'
    login_list = login.split(',')
    uname = login_list[0]
    name = Employee_Info.objects.get(employee_account=uname).employee_name
    return render(request,'top.html',{'curuser':name})


def left_view(request):
    return render(request,'left.html')

def ontime():
    import time
    format = '%m-%d'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    return dt

def center_view(request):
    notice_list = Notice.objects.filter(notice_delete=False).order_by('-notice_id')[:4]
    care_list = Customer_Care.objects.filter(care_is_delete=False).order_by('care_time')[:4]
    date_time = ontime()
    customer_list = Customer_Info.objects.filter(c_is_delete=False)
    dic = {}
    for customer in customer_list:
        val = customer.c_birthdate.strftime('%m/%d')
        if val > date_time:
            c_id = customer.customer_id
            val = customer.c_birthdate
            dic[c_id] = val

    order_tuple = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    list_obj = []
    count = 0
    for order_id in order_tuple:
        for cus in customer_list:
            if cus.customer_id == order_id[0]:
                list_obj.append(cus)
                count = count + 1
                if count > 4:
                    break
                continue

    return render(request, 'center.html', {
        'notice_list': notice_list,
        'care_list': care_list,
        'customer_list': list_obj,
    })


def down_view(request):
    return render(request,'down.html')



def center_info(request):
    query_time1 = request.POST.get('addTime')
    query_time2 = request.POST.get('addTime2')
    on_time = datetime.datetime.now().date()
    # on_moretime = (datetime.datetime.now().date() + datetime.timedelta(days=1))
    care_list = Customer_Care.objects.filter(care_is_delete=False).order_by('care_time')
    notice_list = Notice.objects.filter(notice_delete=False).order_by('-notice_id')[:4]

    if query_time1 == '0':
        care_list = care_list.filter(care_time=on_time)[:4]
    elif query_time1 == '7':
        care_list1 = care_list.filter(care_time__gte=on_time)
        care_list = care_list1.filter(care_time__lt=(on_time + datetime.timedelta(days=7)))[:4]
    elif query_time1 == '15':
        care_list1 = care_list.filter(care_time__gte=on_time)
        care_list = care_list1.filter(care_time__lt=(on_time + datetime.timedelta(days=14)))[:4]
    else:
        care_list1 = care_list.filter(care_time__gte=on_time)
        care_list = care_list1.filter(care_time__lt=(on_time + datetime.timedelta(days=30)))[:4]

    customer_list = Customer_Info.objects.filter(c_is_delete=False)
    sum_dic = {}
    cus_list = []
    cus_list7 = []
    cus_list15 = []
    cus_list30 = []

    for customer in customer_list:
        val = customer.c_birthdate.strftime('%m/%d')

        if val == on_time.strftime('%m/%d'):
            cus_list.append(customer)
        if val < (datetime.datetime.now().date() + datetime.timedelta(days=7)).strftime('%m/%d') and val > (
                datetime.datetime.now().date()).strftime('%m/%d'):
            cus_list7.append(customer)
        if val < (datetime.datetime.now().date() + datetime.timedelta(days=15)).strftime('%m/%d') and val > (
                datetime.datetime.now().date()).strftime('%m/%d'):
            cus_list15.append(customer)
        if val < (datetime.datetime.now().date() + datetime.timedelta(days=30)).strftime('%m/%d') and val > (
                datetime.datetime.now().date()).strftime('%m/%d'):
            cus_list30.append(customer)

    if query_time2 == '0':
        customer_list = cus_list[:4]
    elif query_time2 == '7':
        customer_list = cus_list7[:4]
    elif query_time2 == '15':
        customer_list = cus_list15[:4]
    else:
        customer_list = cus_list30[:4]

    return render(request, 'center.html', {
        'notice_list': notice_list,
        'care_list': care_list,
        'customer_list': customer_list,
    })
