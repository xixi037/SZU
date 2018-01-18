# coding: utf-8
from django.shortcuts import HttpResponseRedirect
import re

EXCLUDE_URL =  (
     '/login',
    '/admin/login',
    '/static',
    '/check',
    '/admin/check',
)    #不需要经过中间件验证的url（其实每个请求都会经过中间件，只是这些在中间件中我们让它不执行验证有无cookie操作）
exclued_path = [re.compile(item) for item in EXCLUDE_URL]

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x

class PubAuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        url_path = request.path
        for each in exclued_path:
            if re.match(each, url_path):
                return         #不需要验证的直接返回
        if request.COOKIES.get('username', '') != '':
            print(request.COOKIES.get('username'))
            pass    #有cookie的直接继续执行
        else:
            return HttpResponseRedirect('login')   #没有cookie的跳转登录页面