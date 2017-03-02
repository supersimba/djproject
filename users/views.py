#coding:utf-8

from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic import View

from .models import UserProfile

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(req):
    if req.method=='POST':
        user_name=req.POST.get("username", "")
        user_word=req.POST.get("password", "")
        user=authenticate(username=user_name,password=user_word)
        if user is not None:
            login(req,user)
            print 'login ok'
            return render(req,"index.html",{})
        else:
            print 'user ===',user
            return render(req, "login.html", {'msg':'登录失败!'})
    elif req.method=='GET':
        return render(req,"login.html",{})