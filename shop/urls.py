from django.urls import path, register_converter
from .converters import FourDigitYearConverter
from . import views

register_converter(FourDigitYearConverter, 'yyyy') #'yyyy'라는 수를 FourDigitYearConverter에 넣어 4자리로 변환

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year), #'yyyy'의 변환된 형태를 year라는 변수에 저장하고, 'archives/year'라는 url이 호출되면 views.py에서 archives_year함수를 호출
    path('', views.item_list),
]