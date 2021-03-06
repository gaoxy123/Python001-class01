from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .form import LoginForms


def index(request):
    return HttpResponse('Hello Django!')


def login_page(request):
    if request.method == 'GET':
        login_form = LoginForms()
        return render(request, 'login_form.html', {'form': login_form})
    elif request.method == 'POST':
        login_form = LoginForms(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
