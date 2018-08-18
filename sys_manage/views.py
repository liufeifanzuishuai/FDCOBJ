# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from db_manager.models import *

# Create your views here.
from .models import *

def jiebao(request,userName,userNum,userAge,userPw,userSex,userNation,userDiploma,isMarried,userTel,
           userIntest,userBankcard,userMobile,userIdnum,userAddress,userAddman,userEmail,departmentId,
           roleId,**kwargs):
    print userName,userNum,userAge,userPw,userSex,userNation,userDiploma,isMarried,userTel,userIntest,userBankcard,userMobile,userIdnum,userAddress,userAddman,userEmail,departmentId,roleId
    person = Employee_Info.objects.filter(employee_identity_card=userIdnum)
    if person:
        return False
    else:
        dep = Department_Info.objects.get(department_id=departmentId[0])
        ro = Role.objects.get(role_id=roleId[0])
        Employee_Info.objects.create(employee_name=userName[0],employee_account=userNum[0],employee_age=userAge[0],employee_password=userPw[0],employee_gender=userSex[0],employee_nation=userNation[0],
                                     employee_education=userDiploma[0],employee_marry=isMarried[0],employee_telephone=userTel[0],
                                     employee_hobby=userIntest[0],employee_wages_card=userBankcard[0],employee_mobile=userMobile[0],employee_identity_card=userIdnum[0],employee_address=userAddress[0],employee_founder=userAddman[0],employee_email=userEmail[0],employee_department=dep,employee_role=ro)
        return True

def employee_view(request):
    if request.method=='GET':
        role_list = Role.objects.all()
        print Role.objects.all()
        department_list = Department_Info.objects.all()
        print department_list
        return render(request,'emp_add.html',{'role_list':role_list,'department_list':department_list})
    else:
        print 'hello'
        if jiebao(request,**request.POST):
            return render(request, 'add_successful.html')
        else:
            return render(request, 'add_failed.html')


def role_view(request):
    if request.method=='GET':
        return render(request,'role_add.html')
    else:
        rname =  request.POST.get('roleName')
        rgrade =  request.POST.get('rolePower')

        if rname and rgrade :
            roleList = Role.objects.filter(role_name=rname)
            if roleList:
                return render(request,'add_failed.html')
            else:
                Role.objects.create(role_name=rname,role_grade=rgrade)
                return render(request,'add_successful.html')
        else:
            return render(request, 'add_failed.html')

def department_view(request):
    if request.method=='GET':
        return render(request,'dept_add.html')
    else:
        dname = request.POST.get('departmentName','')
        dintroduce = request.POST.get('departmentDesc','')
        if dname and dintroduce:
            departmentList = Department_Info.objects.filter(department_name=dname)
            if departmentList:
                return render(request, 'add_failed.html')
            else:
                Department_Info.objects.create(department_name=dname,department_describe=dintroduce)
                return render(request, 'add_successful.html')
        else:
            return render(request, 'add_failed.html')


def look_role_view(request):
    role_list = Role.objects.all()
    return render(request,'look_role.html',{'role_list':role_list})