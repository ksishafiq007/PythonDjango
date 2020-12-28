# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def user_log(request):
    return render(request,'./auth/login.html',{})