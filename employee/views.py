# coding=utf-8
from __future__ import unicode_literals

import math
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.views import View

from db_manager.models import *
from django.shortcuts import render, redirect


# 定义分页函数
def pages(employ_list, num):
    num = int(num)
    pageobj = Paginator(employ_list, 3)
    pageall = pageobj.num_pages
    if num > pageall:
        num = pageall
    if num < 1:
        num = 1
    employ_list = pageobj.page(num)
    return employ_list, pageall


# 员工的信息展示, 与查询
class Employinfo(View):
    def get(self, request, *args, **kwargs):
        employ_list = Employee_Info.objects.filter(employee_delete=False)
        num = request.GET.get('num', 1)
        print('employ num', num)
        employ_list, pageall = pages(employ_list, num)
        if pageall < int(num):
            num = pageall
        return render(request, 'employeeinfo.html', {'employ_list': employ_list, 'pages': pageall, 'num': num})

    def post(self, request, *args, **kwargs):
        query_value = request.POST.get('queryType')
        query_form = request.POST.get('userName', None)
        print('aaa', query_form, query_value)
        if len(query_form) == 0:
            return redirect('/employee/employinfo/')
        if query_value == '1':
            employ_list = Employee_Info.objects.filter(employee_name__contains=query_form).filter(employee_delete=False)
        elif query_value == '2':
            dapart_id = Department_Info.objects.filter(department_name__contains=query_form)
            employ_list = Employee_Info.objects.filter(employee_department=dapart_id).filter(employee_delete=False)
        elif query_value == '3':
            role_id = Role.objects.filter(role_name__contains=query_form)
            employ_list = Employee_Info.objects.filter(employee_role=role_id).filter(employee_delete=False)
        else:
            employ_list = Employee_Info.objects.filter(employee_education__contains=query_form).filter(
                employee_delete=False)

        if employ_list.count() == 0:
            return redirect('/employee/employinfo/')
        else:
            num = request.POST.get('num', 1)
            employ_list, pageall = pages(employ_list, num)
            return render(request, 'employeeinfo.html', {'employ_list': employ_list, 'pages': pageall})


# 员工的信息编辑
class Edit(View):
    def get(self, request, *args, **kwargs):
        query_id = request.GET.get('id')
        employ = Employee_Info.objects.filter(employee_id=query_id).first()
        dapart_list = Department_Info.objects.all()
        return render(request, 'employeeedit.html', {'employee': employ, 'daparts': dapart_list})

    def post(self, request, *args, **kwargs):
        query_dict = request.POST
        user_id = query_dict.get('userId')
        user_age = query_dict.get('userAge')
        user_nation = query_dict.get('userNation', '汉')
        user_diploma = query_dict.get('userDiploma')
        user_department = query_dict.get('departmentId')
        user_tel = query_dict.get('userTel')
        user_interest = query_dict.get('userIntest')
        user_bankcard = query_dict.get('userBankcard')
        user_mobile = query_dict.get('userMobile')
        user_idnum = query_dict.get('userIdnum')
        user_email = query_dict.get('userEmail')
        user_address = query_dict.get('userAddress')
        depart_obj = Department_Info.objects.filter(department_name=user_department).filter(
            department_delete=False).first()

        current_obj = Employee_Info.objects.filter(employee_id=user_id).update(
            employee_age=int(user_age),
            employee_nation=user_nation,
            employee_education=user_diploma,
            employee_telephone=user_tel,
            employee_hobby=user_interest,
            employee_wages_card=user_bankcard,
            employee_mobile=user_mobile,
            employee_email=user_email,
            employee_address=user_address,
            employee_identity_card=user_idnum,
            employee_department=depart_obj,
        )
        return redirect('/employee/employinfo/', {'employee': current_obj})


# 员工的详细信息展示
def detail(request):
    query_id = request.GET.get('id')
    query_obj = Employee_Info.objects.filter(employee_id=int(query_id)).first()
    return render(request, 'employeedetail.html', {'employee': query_obj})


# 员工信息的删除
def delete(request):
    query_id = request.GET.get('id')
    query_obj = Employee_Info.objects.filter(employee_id=int(query_id)).first()
    query_obj.employee_delete = '1'
    query_obj.save()
    return HttpResponse(' 删除成功 ! ')


# 房屋的信息展示, 与查询
class Houseinfo(View):
    def get(self, request, *args, **kwargs):
        house_list = House.objects.filter(house_delete=False)
        num = request.GET.get('num', 1)
        house_list, pageall = pages(house_list, num)
        if pageall < int(num):
            num = pageall
        return render(request, 'houseinfo.html', {'house_list': house_list, 'pages': pageall, 'num': num})

    def post(self, request, *args, **kwargs):
        query_value = request.POST.get('houseInput','')
        query_form = request.POST.get('queryType', '')
        print 'aaa', query_form, query_value
        if query_value is '':
            return redirect('/employee/houseinfo')

        if query_form == '1':
            house_typelist = House_Type.objects.filter(h_type_name__exact=query_value)
            if house_typelist.count() == 0:
                return redirect('/employee/houseinfo')
            house_list = House.objects.filter(house_housetype=house_typelist).filter(house_delete=False)
        else:
            house_list = House.objects.filter(house_address__contains=query_value).filter(house_delete=False)

        if len(house_list) == 0:
            return redirect('/employee/houseinfo')
        else:
            num = request.POST.get('num', 1)
            house_list, pageall = pages(house_list, num)
            return render(request, 'houseinfo.html', {'house_list': house_list, 'pages': pageall})


# 房屋的信息添加
class Houseadd(View):
    def get(self, request, *args, **kwargs):
        house_typelist = House_Type.objects.filter(h_type_delete=False)
        members = Employee_Info.objects.values('employee_name').filter(employee_delete=False)
        return render(request, 'houseadd.html', {'house_types': house_typelist, 'members': members})

    def post(self, request, *args, **kwargs):
        house_type = request.POST.get('housetype')
        house_manager = request.POST.get('housemanager')
        house_address = request.POST.get('houseaddress', None)
        house_env = request.POST.get('houseenv', None)
        house_price = request.POST.get('houseprice', None)

        if len(house_address) == 0 or len(house_env) == 0 or len(house_price) == 0:
            return redirect('/employee/houseinfo')
        else:
            house_price = float(house_price)
            type_obj = House_Type.objects.filter(h_type_name=house_type).filter(h_type_delete=False).first()
            manager_obj = Employee_Info.objects.filter(employee_name=house_manager).filter(employee_delete=False).first()
            new_houseadd = House.objects.create(
                house_address=house_address,
                house_price=house_price,
                house_environment=house_env,
                house_type=house_type,
                house_employee=manager_obj,
                house_housetype=type_obj,
            )
            return redirect('/employee/houseinfo')


# 房屋的信息编辑
class Houseedit(View):
    def get(self, request, *args, **kwargs):
        house_id = request.GET.get('id')
        house_obj = House.objects.filter(house_id=int(house_id)).first()
        house_typelist = House_Type.objects.filter(h_type_delete=False)
        members = Employee_Info.objects.values('employee_name').filter(employee_delete=False)
        return render(request, 'houseedit.html',
                      {'house': house_obj, 'house_types': house_typelist, 'members': members})

    def post(self, request, *args, **kwargs):
        house_type = request.POST.get('housetype')
        house_manager = request.POST.get('housemanager')
        house_address = request.POST.get('houseaddress', None)
        house_env = request.POST.get('houseenv', None)
        house_price = request.POST.get('houseprice', None)
        house_price = float(house_price)
        house_id = int(request.POST.get('houseid'))

        if house_address is None or house_env is None or house_price is None:
            return redirect('/employee/houseinfo')
        else:
            type_obj = House_Type.objects.get(h_type_name=house_type)
            manager_obj = Employee_Info.objects.get(employee_name=house_manager)

            house_obj = House.objects.filter(house_id=house_id).update(
                house_address=house_address,
                house_price=house_price,
                house_environment=house_env,
                house_type=house_type,
                house_employee=manager_obj,
                house_housetype=type_obj,
            )
            return redirect('/employee/houseinfo')


# 房屋的信息删除
def housedelete(request):
    house_id = int(request.GET.get('id'))
    house_obj = House.objects.filter(house_id=house_id).first()
    house_obj.house_delete = '1'
    house_obj.save()
    return redirect('/employee/houseinfo')


# 房屋类型的信息展示, 与查询
class Housetypeinfo(View):
    def get(self, request, *args, **kwargs):
        type_list = House_Type.objects.filter(h_type_delete=False)
        num = request.GET.get('num', 1)
        type_list, pageall = pages(type_list, num)
        if pageall < int(num):
            num = pageall
        return render(request, 'housetype.html', {'type_list': type_list, 'pages': pageall, 'num': num})

    def post(self, request, *args, **kwargs):
        query_value = request.POST.get('houseTypeName', None)
        if query_value is None:
            return redirect('/employee/housetypeinfo')

        type_list = House_Type.objects.filter(h_type_name__contains=query_value).filter(h_type_delete=False)
        if type_list.count() == 0:
            return redirect('/employee/housetypeinfo')
        else:
            num = request.POST.get('num', 1)
            type_list, pageall = pages(type_list, num)
            return render(request, 'housetype.html', {'type_list': type_list, 'pages': pageall})


# 房屋类型的信息添加
class Housetypeadd(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'housetypeadd.html')

    def post(self, request, *args, **kwargs):
        type_name = request.POST.get('housetypename', None)
        if len(type_name) == 0 or type_name is None:
            return redirect('/employee/housetypeinfo')
        try:
            typeobj = House_Type.objects.get(h_type_name=type_name)
        except:
            typeobj = House_Type.objects.create(h_type_name=type_name)
        return redirect('/employee/housetypeinfo')


# 房屋类型的删除
def housetypedelete(request):
    type_id = int(request.GET.get('id'))
    print('ID..', type_id)
    type_obj = House_Type.objects.filter(h_type_id=type_id).first()
    type_obj.h_type_delete = '1'
    type_obj.save()
    return redirect('/employee/housetypeinfo')


# 公告的信息展示, 与查询
class Notices(View):
    def get(self, request, *args, **kwargs):
        notice_list = Notice.objects.filter(notice_delete=False)
        num = request.GET.get('num', 1)
        notice_list, pageall = pages(notice_list, num)
        if pageall < int(num):
            num = pageall
        return render(request, 'notice.html', {'notice_list': notice_list, 'pages': pageall, 'num': num})

    def post(self, request, *args, **kwargs):
        query_value = request.POST.get('noticeInput', None)
        query_form = request.POST.get('queryType')
        print query_value
        if query_value is None:
            return redirect('/employee/notice')
        if query_form == '1':
            notice_list = Notice.objects.filter(notice_theme__contains=query_value).filter(notice_delete=False)
        else:
            notice_list = Notice.objects.filter(notice_content__contains=query_value).filter(notice_delete=False)
        if notice_list.count() == 0:
            return redirect('/employee/notice')
        else:
            num = request.POST.get('num', 1)
            notice_list, pageall = pages(notice_list, num)
            return render(request, 'notice.html', {'notice_list': notice_list, 'pages': pageall})


# 公告的信息添加
class Noticesadd(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'noticeadd.html')

    def post(self, request, *args, **kwargs):
        notice_theme = request.POST.get('noticetheme', None)
        notice_man = request.POST.get('noticeman', None)
        notice_content = request.POST.get('noticecontent', None)
        notice_deltime = request.POST.get('noticedetime', None)
        flag = False
        import time
        format = "%Y-%m-%d"
        value = time.localtime(int(time.time()))
        dt = time.strftime(format, value)
        print(notice_deltime, dt)
        if dt > notice_deltime:
            flag = True
        if flag:
            return redirect('/employee/notice')
        if notice_theme is None or notice_man is None or notice_content is None or notice_deltime is None:
            return redirect('/employee/notice')
        else:
            new_notice = Notice.objects.create(
                notice_theme=notice_theme,
                notice_content=notice_content,
                notice_end_time=notice_deltime,
                notice_man=notice_man,
            )
            print('guaua')
            return redirect('/employee/notice')


# 公告的信息删除
def noticedelete(request):
    notice_id = int(request.GET.get('id'))
    notice_obj = Notice.objects.filter(notice_id=notice_id).first()
    notice_obj.notice_delete = '1'
    notice_obj.save()
    return redirect('/employee/notice')


# 部门的信息展示, 与查询
class Department(View):
    def get(self, request, *args, **kwargs):
        depart_list = Department_Info.objects.filter(department_delete=False)
        num = request.GET.get('num', 1)
        depart_list, pageall = pages(depart_list, num)
        if pageall < int(num):
            num = pageall
        return render(request, 'department.html', {'depart_list': depart_list, 'pages': pageall, 'num': num})

    def post(self, request, *args, **kwargs):
        query_value = request.POST.get('departmentName', None)

        if query_value is None:
            return redirect('/employee/department')
        depart_list = Department_Info.objects.filter(department_name__contains=query_value).filter(
            department_delete=False)
        if depart_list.count() == 0:
            return redirect('/employee/department')
        else:
            num = request.POST.get('num', 1)
            depart_list, pageall = pages(depart_list, num)
            return render(request, 'department.html', {'depart_list': depart_list, 'pages': pageall})


# 部门的信息删除
def departmentdelete(request):
    depart_id = int(request.GET.get('id'))
    depart_obj = Department_Info.objects.filter(department_id=depart_id).first()
    employ_list = Employee_Info.objects.filter(employee_department=depart_obj).filter(employee_delete=False)

    if len(employ_list) != 0:
        for employee in employ_list:
            employee.employee_delete = '1'
            employee.save()
    depart_obj.department_delete = '1'
    depart_obj.save()
    return redirect('/employee/department')
