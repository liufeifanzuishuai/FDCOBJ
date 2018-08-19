# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View

from .models import *
# Create your views here.
# 分页
def paging(request,tablename):
    num = request.GET.get('num', 1)
    if num == '':
        num = 1
    num = int(num)
    # 获取所有的员工信息
    list_all = tablename
    # 创建分页对象
    page_obj = Paginator(list_all, 3)
    # 获取页面数据
    list_page = page_obj.page(num)
    counter = len(list_page)
    # 总页数
    page_counter = page_obj.num_pages
    return num,list_page,counter,page_counter

# 定义分页函数2
def pages(employ_list, num):
    num = int(num)
    pageobj = Paginator(employ_list, 24)
    pageall = pageobj.num_pages
    if num > pageall:
        num = pageall
    if num < 1:
        num = 1
    employ_list = pageobj.page(num)
    return employ_list, pageall


## 显示客户信息页面
def show_info(request):
    customer_list = Customer_Info.objects.filter(c_is_delete=False)
    num, list_page, counter, page_counter=paging(request,customer_list)
    return render(request,'customer_list1.html',{'cus_list':list_page,'counter':counter,'page_counter':page_counter,'num':num})

# 查询客户信息
def select_customer(request):
    queryway=request.GET.get('queryway')
    querycontent=request.GET.get('querycontent')
    # 客户姓名
    if queryway=='1':

        customer_list = Customer_Info.objects.filter(c_name__contains=querycontent,c_is_delete=False)

        num, list_page, counter, page_counter = paging(request, customer_list)
        return render(request, 'customer_list1.html',
                      {'cus_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

    # 客户状态
    elif queryway=='2':
        customer_state_list = customer_State.objects.filter(c_state_name__contains=querycontent)
        customer_list1=[]
        for c in customer_state_list:
            customer_list1+=c.customer_info_set.filter(c_is_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_list1)
        return render(request, 'customer_list1.html',
                      {'cus_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

    # 客户来源
    elif queryway=='3':
        customer_source_list = Customer_Source.objects.filter(c_source_name__contains=querycontent)
        customer_list1 = []
        for c in customer_source_list:
            customer_list1 += c.customer_info_set.filter(c_is_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_list1)
        return render(request, 'customer_list1.html',
                      {'cus_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

    # 客户类型
    elif queryway=='4':
        customer_type_list = Customer_Type.objects.filter(c_type_name__contains=querycontent)
        customer_list1 = []
        for c in customer_type_list:
            customer_list1 += c.customer_info_set.filter(c_is_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_list1)
        return render(request, 'customer_list1.html',
                      {'cus_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

    #所属员工
    elif queryway=='5':
        employee_name_list = Employee_Info.objects.filter(employee_name__contains=querycontent)
        customer_list1 = []
        for c in employee_name_list:
            customer_list1 += c.customer_info_set.filter(c_is_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_list1)
        return render(request, 'customer_list1.html',
                      {'cus_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

    # 所属公司
    elif queryway=='6':
        customer_list = Customer_Info.objects.filter(c_company__contains=querycontent,c_is_delete=False)

        num, list_page, counter, page_counter = paging(request, customer_list)
        return render(request, 'customer_list1.html',
                      {'cus_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})


# 添加客户信息页面
def addinfo_view(request):
    # 客户来源
    source_list = Customer_Source.objects.filter(c_source_delete=False)
    # 类型
    type_list = Customer_Type.objects.filter(c_type_delete=False)
    # 状态
    state_list = customer_State.objects.filter(c_state_delete=False)
    return render(request,'customer_add.html',{'source_list':source_list,'type_list':type_list,'state_list':state_list})


def addinfo(c_name,c_gender,c_birthdate,c_mobile,c_address,c_founder,c_telephone,c_company,c_email,c_QQ,c_change_people,
               c_weibo,c_MSN,c_remark,c_profession,c_type,c_source,c_state,**kwargs):
    cus_type=Customer_Type.objects.get(c_type_name=c_type[0])
    cus_emp=Employee_Info.objects.get(employee_name=c_founder[0])
    cus_source=Customer_Source.objects.get(c_source_name=c_source[0])
    cus_state=customer_State.objects.get(c_state_name=c_state[0])
    Customer_Info.objects.create(c_name=c_name[0],
                                    c_gender=c_gender[0],
                                    c_birthdate=c_birthdate[0],
                                    c_mobile=c_mobile[0],
                                    c_address=c_address[0],
                                    c_founder=c_founder[0],
                                    c_telephone=c_telephone[0],
                                    c_company=c_company[0],
                                    c_email=c_email[0],
                                    c_QQ=c_QQ[0],
                                    c_change_people=c_change_people[0],
                                    c_weibo=c_weibo[0],
                                    c_MSN=c_MSN[0],
                                    c_remark=c_remark[0],
                                    c_profession=c_profession[0],
                                    c_type=c_type[0],
                                    cus_emp=cus_emp,
                                    cus_type=cus_type,
                                    cus_source=cus_source,
                                    cus_state=cus_state,)

# 添加客户信息
def addcustomer_view(request):
    addinfo(**request.POST)
    return HttpResponseRedirect('/customer/showinfo/')

def eidt_info(customer_id,c_gender,c_mobile,c_address,c_telephone,c_company,c_email,c_QQ,c_change_people,
    c_weibo,c_MSN,c_remark,c_profession,c_type,c_emp,c_source,c_state,**kwargs):
        cus_type=Customer_Type.objects.get(c_type_id=c_type[0])
        cus_emp=Employee_Info.objects.get(employee_id=c_emp[0])
        cus_source=Customer_Source.objects.get(c_source_id=c_source[0])
        cus_state=customer_State.objects.get(c_state_id=c_state[0])
        customer=Customer_Info.objects.get(customer_id=customer_id[0])
        customer.c_gender = c_gender[0]
        customer.c_mobile = c_mobile[0]
        customer.c_address = c_address[0]
        customer.c_telephone = c_telephone[0]
        customer.c_company = c_company[0]
        customer.c_email = c_email[0]
        customer.c_QQ = c_QQ[0]
        customer.c_change_people = c_change_people[0]
        customer.c_weibo = c_weibo[0]
        customer.c_MSN = c_MSN[0]
        customer.c_remark = c_remark[0]
        customer.c_profession = c_profession[0]
        customer.c_type = c_type[0]
        customer.cus_type=cus_type
        customer.cus_emp = cus_emp
        customer.cus_source = cus_source
        customer.cus_state = cus_state
        customer.save()


# 编辑客户信息页面
def eidt_view(request):
    if request.method=='GET':
        customer_id=request.GET.get('customer_id')
        customer=Customer_Info.objects.get(customer_id=customer_id)
        # 员工
        employee_list=Employee_Info.objects.filter(employee_delete=False)
        # 客户来源
        source_list=Customer_Source.objects.filter(c_source_delete=False)
        # 类型
        type_list=Customer_Type.objects.filter(c_type_delete=False)
        # 状态
        state_list=customer_State.objects.filter(c_state_delete=False)

        return render(request,'customer_edit.html',{'customer':customer,'employee_list':employee_list,'source_list':source_list,'type_list':type_list,'state_list':state_list})

    else:
        eidt_info(**request.POST)
        return HttpResponseRedirect('/customer/showinfo/')


# 显示客户详细信息
def detail_view(request):
    custmer_id=request.GET.get('customer_id')
    customer=Customer_Info.objects.get(customer_id=custmer_id)
    return render(request,'customer_detail.html',{'customer':customer})

# 删除客户信息
def del_customer(request):
    customer_id=request.GET.get('customer_id')
    customer=Customer_Info.objects.get(customer_id=customer_id)
    customer.c_is_delete=True
    customer.save()
    return HttpResponseRedirect('/customer/showinfo/')


## 客户类型
def type_view(request):
    if request.method=='GET':
        customer_type = Customer_Type.objects.filter(c_type_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_type)
        return render(request, 'customer_type_list.html',
                      {'ty_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})
    else:
        typename = request.POST.get('TypeName')
        customer_type = Customer_Type.objects.filter(c_type_name__contains=typename,c_type_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_type)
        return render(request, 'customer_type_list.html',
                      {'ty_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

# 客户类型的添加
def type_add(request):
    if request.method=='GET':
        return render(request,'customer_type_add.html')
    else:
        c_type_name=request.POST.get('c_type_name')
        Customer_Type.objects.create(c_type_name=c_type_name)
        return HttpResponseRedirect('/customer/customer_type/')

# 删除客户类型
def del_type(request):
    c_type_id=request.GET.get('c_type_id')
    type=Customer_Type.objects.get(c_type_id=c_type_id)
    type.c_type_delete=True
    type.save()
    return HttpResponseRedirect('/customer/customer_type/')

## 客户状态
def state_view(request):
    if request.method=='GET':
        customer_state_list = customer_State.objects.filter(c_state_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_state_list)
        return render(request, 'customer_state_list.html',
                      {'st_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})
    else:
        ConditionName = request.POST.get('ConditionName')
        customer_state_list = customer_State.objects.filter(c_state_name__contains=ConditionName,c_state_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_state_list)
        return render(request, 'customer_state_list.html',
                      {'st_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

# 客户状态添加
def state_add(request):
    if request.method=='GET':
        return render(request,'customer_state_add.html')
    else:
        c_state_name=request.POST.get('c_state_name')
        c_state_descripe=request.POST.get('c_state_descripe')
        customer_State.objects.create(c_state_name=c_state_name,c_state_descripe=c_state_descripe)
        return HttpResponseRedirect('/customer/customer_state/')

# 状态删除
def del_state(request):
    c_state_id=request.GET.get('c_state_id')
    state=customer_State.objects.get(c_state_id=c_state_id)
    state.c_state_delete=True
    state.save()
    return HttpResponseRedirect('/customer/customer_state/')

## 客户来源
def source_view(request):
    if request.method=='GET':
        customer_source_list = Customer_Source.objects.filter(c_source_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_source_list)
        return render(request, 'customer_source_list.html',
                      {'so_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})
    else:
        SourceName = request.POST.get('SourceName')
        customer_source_list = Customer_Source.objects.filter(c_source_name__contains=SourceName,c_source_delete=False)
        num, list_page, counter, page_counter = paging(request, customer_source_list)
        return render(request, 'customer_source_list.html',
                      {'so_list': list_page, 'counter': counter, 'page_counter': page_counter, 'num': num})

# 来源添加
def source_add(request):
    if request.method=='GET':
        return render(request,'customer_source_add.html')
    else:
        c_source_name=request.POST.get('c_source_name')
        Customer_Source.objects.create(c_source_name=c_source_name)
        return HttpResponseRedirect('/customer/customer_source/')

# 来源删除
def del_source(request):
    c_source_id=request.GET.get('c_source_id')
    source=Customer_Source.objects.get(c_source_id=c_source_id)
    source.c_source_delete=True
    source.save()
    return HttpResponseRedirect('/customer/customer_source/')


class Distribute(View):
    def get(self,request,*args,**kwargs):
        #获取没有被删除的客户
        customer_Info_list = Customer_Info.objects.filter(c_is_delete=False)
        num=request.GET.get('num',1)
        customer_Info_list, pageall = pages(customer_Info_list, num)
        if pageall < int(num):
            num = pageall
        # 客户信息表的列表长度
        count = len(customer_Info_list)
        return render(request, 'customer_distribute_list.html',{"customer_Info_lsit": customer_Info_list, "count": count,'pages':pageall,'num':num})


def singledis(request):
    customer=request.GET.get('customer')
    if request.method=="GET":
        allemp=Employee_Info.objects.all()
        return render(request,'distribute.html',{'customer':customer,'allemp':allemp})
    else:
        result=request.POST.get('Distribute')
        Customer_Info.objects.filter(c_name=customer).update(c_founder=result)
    return HttpResponse('提交成功')



## 客户关怀
def care_view(request):
    if request.method=='GET':
        care_list=Customer_Care.objects.filter(care_is_delete=False)
        num, list_page, counter, page_counter=paging(request,care_list)
        return render(request,'customer_care_list.html',
                        {'care_list':list_page,'num':num,'list_page':list_page,'counter':counter,'page_counter':page_counter})
    else:
        query_content=request.POST.get('query_content')
        query_way=request.POST.get('query_way')
        care_list1=None
        # 关怀客户
        if query_way=='1':
            care_list1=Customer_Care.objects.filter(cus_care__c_name__contains=query_content,care_is_delete=False)
        # 关怀主题
        elif query_way=='2':
            care_list1=Customer_Care.objects.filter(care_theme__contains=query_content,care_is_delete=False)
        # 关怀方式
        elif query_way=='3':
            care_list1=Customer_Care.objects.filter(care_way__contains=query_content,care_is_delete=False)

        num, list_page, counter, page_counter = paging(request, care_list1)
        return render(request, 'customer_care_list.html',
                      {'care_list': list_page, 'num': num, 'list_page': list_page, 'counter': counter,
                       'page_counter': page_counter})


def add_careinfo(care_theme,c_care,care_time,careNexttime1,careWay,care_remark,**kwargs):
    cus_care=Customer_Info.objects.get(customer_id=c_care[0])
    Customer_Care.objects.create(care_theme=care_theme[0],
                                    care_time=care_time[0],
                                    care_nexttime=careNexttime1[0],
                                    care_way=careWay[0],
                                    care_remark=care_remark[0],
                                    cus_care=cus_care,
                                 )

def update_care(care_theme,c_care,care_time,careNexttime1,careWay,care_remark,**kwargs):
    care=Customer_Care.objects.get(cus_care_id=c_care[0])
    care.care_theme = care_theme[0]
    care.care_time = care_time[0]
    care.care_nexttime = careNexttime1[0]
    care.care_way = careWay[0]
    care.care_remark = care_remark[0]
    care.care_is_delete=False
    care.save()

# 关怀添加
def care_add(request):
    if request.method=='GET':
        care_list=Customer_Care.objects.filter(care_is_delete=False)
        customer_list=Customer_Info.objects.filter(c_is_delete=False)
        carelist = []
        customerlist=[]
        for customer in customer_list:
            customerlist.append(customer)
            for care in care_list:
                carelist.append(care)
                if customer.customer_id == care.cus_care_id:
                    customerlist.remove(customer)
        return render(request,'customer_care_add.html',{'customer_list':customerlist})

    else:
        customer_id=request.POST.get('c_care')
        care=Customer_Care.objects.filter(cus_care_id=customer_id)
        if care.count()==0:
            add_careinfo(**request.POST)
        else:
            update_care(**request.POST)
        return HttpResponseRedirect('/customer/customer_care/')


def care_eidt_info(care_id,care_theme,c_care,care_nexttime,care_way,care_remark,**kwargs):
    care=Customer_Care.objects.get(care_id=care_id[0])
    cus_care=Customer_Info.objects.get(c_name=c_care[0])

    care.care_theme = care_theme[0]
    care.care_nexttime = care_nexttime[0]
    care.care_way = care_way[0]
    care.care_remark = care_remark[0]
    care.cus_care = cus_care

    care.save()

# 关怀编辑
def care_eidt(request):
    if request.method=='GET':
        care_id=request.GET.get('care_id')
        care1=Customer_Care.objects.get(care_id=care_id)

        care_list = Customer_Care.objects.filter(care_is_delete=False)
        customer_list = Customer_Info.objects.filter(c_is_delete=False)
        carelist = []
        customerlist = []
        for customer in customer_list:
            customerlist.append(customer)
            for care in care_list:
                carelist.append(care)
                if customer.customer_id == care.cus_care_id:
                    customerlist.remove(customer)
        customerlist.append(care1.cus_care)

        return render(request,'customer_care_edit.html',{'care1':care1,'customerlist':customerlist})

    else:
        print request.POST
        care_eidt_info(**request.POST)
        return HttpResponseRedirect('/customer/customer_care/')

# 删除关怀
def del_care(request):
    care_id=request.GET.get('care_id')
    care=Customer_Care.objects.get(care_id=care_id)
    care.care_is_delete=True
    care.save()
    return HttpResponseRedirect('/customer/customer_care/')