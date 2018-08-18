# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from db_manager.models import Employee_Info,Customer_Info


class Distribute(View):
    def get(self,request,*args,**kwargs):
        customer_Info_list = Customer_Info.objects.all()
        # 客户信息表的列表长度
        count = len(customer_Info_list)
        return render(request, 'customer_distribute_list.html',{"customer_Info_lsit": customer_Info_list, "count": count})


def singledis(request):
    customer=request.GET.get('customer')
    if request.method=="GET":
        allemp=Employee_Info.objects.all()
        return render(request,'distribute.html',{'customer':customer,'allemp':allemp})
    else:
        result=request.POST.get('Distribute')
        Customer_Info.objects.filter(c_name=customer).update(c_name=result)
    return HttpResponse('提交成功')




