from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year)) #url.py에서 archives_year 함수가 호출되면 'year년도에 대한 내용'이라는 내용을 return 하여 보여준다.