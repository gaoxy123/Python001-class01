from django.urls import path, re_path, register_converter
from . import views, converters


register_converter(converters.IntConverter,'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', views.index),
    path('info', views.info),
    path('<int:year>/<str:name>', views.name),
    path('<yyyy:year>', views.year),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
]
