from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Name
# Create your views here.


def index(request):
    return HttpResponse('hello django!')


def name(request, **kwargs):
    return HttpResponse(kwargs.values())


def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')


def myyear(request, year):
    return render(request, 'yearview.html', context={'urlyear': year})


def info(request):
    n = Name.objects.all()
    return render(request, 'infoslist.html', locals())

