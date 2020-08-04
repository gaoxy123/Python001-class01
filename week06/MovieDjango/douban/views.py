from django.shortcuts import render
from django.db.models import Avg
from django.http import HttpResponseNotFound
from traceback import format_exc
import json

from .models import T1, DouBanMovie

# Create your views here.


def douban_movie_show(request):
    shorts = T1.objects.all()
    counter = T1.objects.all().count()
    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())


def huozhe_movie_show(request):
    try:
        movie_shorts = DouBanMovie.objects.filter(movie_name='活着', n_star__gt=3)
        return render(request, 'douban_movie.html', locals())
    except:
        return HttpResponseNotFound(f"<h1>发生未知异常{format_exc()}</h1>")
