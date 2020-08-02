from django.urls import path
from . import views


urlpatterns = [
    path('index', views.douban_movie_show),
    path('movie/huozhe', views.huozhe_movie_show)
]
