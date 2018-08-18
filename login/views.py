# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
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