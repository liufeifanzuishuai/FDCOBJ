#coding=utf-8
from django.conf.urls import url
import  views

urlpatterns=[
    ## 显示客户的基本信息页面
    url(r'^showinfo/$',views.show_info),
    # 点击添加显示添加页面
    url(r'^customerinfo_add/$',views.addinfo_view),
    # 添加员工
    url(r'^addcustomer/$',views.addcustomer_view),
    # 编辑
    url(r'^edit/',views.eidt_view),
    # 显示客户详情
    url(r'^customer_detail/$',views.detail_view),
    # 查询客户信息
    url(r'^select/$',views.select_customer),
    # 删除客户信息
    url(r'^del_customer/$',views.del_customer),

    ## 客户类型
    url(r'^customer_type/$',views.type_view),
    # 类型添加
    url(r'^type_add/$',views.type_add),
    # 类型删除
    url(r'^del_type/$',views.del_type),

    ## 客户状态
    url(r'^customer_state/$',views.state_view),
    # 状态添加
    url(r'^state_add/$',views.state_add),
    # 状态删除
    url(r'^del_state/$',views.del_state),

    ## 客户来源
    url(r'^customer_source/$',views.source_view),
    # 来源添加
    url(r'^source_add/$',views.source_add),
    # 来源删除
    url(r'^del_source/$',views.del_source),
    url(r'distribute/$',views.Distribute.as_view()),
    url(r'singledis/$',views.singledis),

    ## 客户关怀
    url(r'^customer_care/$',views.care_view),
    # 关怀添加
    url(r'^care_add/$',views.care_add),
    # 关怀编辑
    url(r'^care_edit/$',views.care_eidt),
    # 删除关怀
    url(r'^del_care/$',views.del_care),
]
