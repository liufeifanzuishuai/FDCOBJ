# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# 客户类型表
class Customer_Type(models.Model):
    c_type_id=models.AutoField(primary_key=True)
    c_type_name=models.CharField(max_length=60)
    c_type_delete=models.BooleanField(default=False)

    class Meta:
        db_table = 't_customer_type'

    def __unicode__(self):
        return u'Customer_Type:%s' % self.c_type_name

# 客户来源表
class Customer_Source(models.Model):
    c_source_id=models.AutoField(primary_key=True)
    c_source_name=models.CharField(max_length=60)
    c_source_delete=models.BooleanField(default=False)

    class Meta:
        db_table = 't_customer_source'

    def __unicode__(self):
        return u'Customer_Source:%s' % self.c_source_name

# 客户状态表
class customer_State(models.Model):
    c_state_id=models.AutoField(primary_key=True)
    c_state_name=models.CharField(max_length=60)
    c_state_descripe=models.CharField(max_length=60)
    c_state_delete=models.BooleanField(default=False)

    class Meta:
        db_table = 't_customer_state'

    def __unicode__(self):
        return u'customer_State:%s' % self.c_state_name


# --------------------------------------------------------------------------------


# 部门信息表(表六)
class Department_Info(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=60, blank=True, null=True)
    department_describe = models.CharField(max_length=500, blank=True, null=True)
    department_delete = models.NullBooleanField(blank=True, null=True, default=False)

    class Meta:
        db_table = 't_department'

    def __unicode__(self):
        return u'Department_Info:%s'%self.department_name

# 角色表
class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=60, blank=True, null=True)
    role_grade = models.CharField(max_length=60, blank=True, null=True)
    role_delete = models.NullBooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 't_role'

    def __unicode__(self):
        return u'Role:%s' % self.role_name


# 员工信息表(表七)
class Employee_Info(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=60, blank=True, null=True)
    employee_gender = models.CharField(max_length=60, blank=True, null=True)
    employee_age = models.IntegerField(blank=True, null=True)
    employee_nation = models.CharField(max_length=60, blank=True, null=True)
    employee_wages_card = models.CharField(max_length=60, blank=True, null=True)
    employee_education = models.CharField(max_length=60, blank=True, null=True)
    employee_marry = models.CharField(max_length=10, blank=True, null=True)
    employee_address = models.CharField(max_length=600, blank=True, null=True)
    employee_mobile = models.CharField(max_length=60, blank=True, null=True)
    employee_telephone = models.CharField(max_length=60, blank=True, null=True)
    employee_email = models.CharField(max_length=250, blank=True, null=True)
    employee_identity_card = models.CharField(max_length=60, blank=True, null=True)
    employee_founder = models.CharField(max_length=60, blank=True, null=True)
    employee_account = models.CharField(max_length=60, blank=True, null=True)
    employee_password = models.CharField(max_length=60, blank=True, null=True)
    employee_hobby = models.CharField(max_length=60, blank=True, null=True)
    employee_delete = models.NullBooleanField(default=False, blank=True, null=True)
    #外键
    employee_department = models.ForeignKey(Department_Info)
    employee_role = models.ForeignKey(Role)

    class Meta:
        db_table = 't_employee'

    def __unicode__(self):
        return u'Employee_Info:%s'%self.employee_name

# 房屋类型表(表九)
class House_Type(models.Model):
    h_type_id = models.AutoField(primary_key=True)
    h_type_name = models.CharField(max_length=60, blank=True, null=True)
    h_type_delete = models.NullBooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 't_house_type'

    def __unicode__(self):
        return u'House_Type:%s' % self.h_type_name


# 房屋信息表（表八）
class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    house_address = models.CharField(max_length=100, blank=True, null=True)
    house_price = models.FloatField(blank=True, null=True)
    house_environment = models.CharField(max_length=1000, blank=True, null=True)
    house_type = models.CharField(max_length=100, blank=True, null=True)
    house_delete = models.NullBooleanField(default=False, blank=True, null=True)
    #外键
    house_employee = models.ForeignKey(Employee_Info)
    house_housetype = models.ForeignKey(House_Type)

    class Meta:
        db_table = 't_house'

    def __unicode__(self):
        return u'House:%s'%self.house_type


# 公告表（表十）
class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    notice_theme = models.CharField(max_length=100, blank=True, null=True)
    notice_content = models.CharField(max_length=6000, blank=True, null=True)
    notice_time = models.DateTimeField(auto_now_add=True)
    notice_end_time = models.DateTimeField()
    notice_man = models.CharField(max_length=60, blank=True, null=True)
    notice_delete = models.NullBooleanField(default=False, blank=True, null=True)

    class Meta:
        db_table = 't_notice'

    def __unicode__(self):
        return u'Notice:%s'%self.notice_theme


#-------------------------------------------------------------------------------------------
# 客户信息表
class Customer_Info(models.Model):
    customer_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=60,null=False)
    c_gender=models.CharField(max_length=60,null=False)
    c_birthdate=models.DateField(blank=True,null=True)
    c_mobile=models.CharField(max_length=60,null=False)
    c_address=models.CharField(max_length=60,blank=True,null=True)
    c_founder=models.CharField(max_length=60,null=False)
    c_telephone=models.CharField(max_length=60,blank=True,null=True)
    c_company=models.CharField(max_length=60,blank=True,null=True)
    c_email=models.CharField(max_length=254,blank=True,null=True)
    c_QQ=models.CharField(max_length=60,blank=True,null=True)
    c_change_people=models.CharField(max_length=60,null=False)
    c_weibo=models.CharField(max_length=60,blank=True,null=True)
    c_MSN=models.CharField(max_length=60,blank=True,null=True)
    c_createdate=models.DateTimeField(auto_now_add=True)
    # 备注
    c_remark=models.TextField(blank=True,null=True)
    c_profession=models.CharField(max_length=60,blank=True,null=True)
    c_type=models.CharField(max_length=60,null=False)
    c_is_delete=models.BooleanField(default=False)

    # 外键字段
    # 客户信息表与员工信息表的一对多关系
    cus_emp=models.ForeignKey(Employee_Info)
    # 客户信息表与客户类型表的一对多关系
    cus_type=models.ForeignKey(Customer_Type)
    # 客户信息表与客户来源表的一对多关系
    cus_source=models.ForeignKey(Customer_Source)
    # 客户信息表与客户状态表的一对多关系
    cus_state=models.ForeignKey(customer_State)

    class Meta:
        db_table='t_customer_info'

    def __unicode__(self):
        return u'Customer_Info:%s'%self.c_name


# 客户关怀表
class Customer_Care(models.Model):
    care_id=models.AutoField(primary_key=True)
    care_theme=models.CharField(max_length=60)
    care_way=models.CharField(max_length=60)
    care_time=models.DateField()
    care_nexttime=models.DateField()
    care_remark=models.TextField()
    care_is_delete=models.BooleanField(default=False)

    # 客户信息表与客户关怀表的一对一关系
    cus_care = models.OneToOneField(Customer_Info)


    class Meta:
        db_table = 't_customer_care'

    def __unicode__(self):
        return u'Customer_Care:%s' % self.care_theme



