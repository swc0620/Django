from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.

def archives_year(request, year):
    return HttpResponse('{}년도에 대한 내용'.format(year)) #url.py에서 archives_year 함수가 호출되면 'year년도에 대한 내용'이라는 내용을 return 하여 보여준다.

def item_list(request):
    qs = Item.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    return render(request, 'shop/item_list.html', {
        'item_list' : qs,
        'q':q,
    })

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'shop/item_detail.html', {
        'item': item,
    })