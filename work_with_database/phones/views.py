from django.shortcuts import render, redirect
from django.http import HttpResponse

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    '''При запросе <имя_сайта>/catalog должна открываться страница
    с отображением всех телефонов
    В каталоге необходимо добавить возможность менять порядок отображения товаров:
    по названию в алфавитном порядке и по цене по убыванию и по возрастанию'''
    
    template = 'catalog.html'
    
    all_phones = Phone.objects.all()
    sort_direct = request.GET.get('sort', '')
    print(f'{all_phones=}, {sort_direct=}')
    
    if sort_direct == 'max_price':
        all_phones = all_phones.order_by('-price')
        
    elif sort_direct == 'min_price':
        all_phones = all_phones.order_by('price')
    
    elif sort_direct == 'name':
        all_phones = all_phones.order_by('name')
    
    context = {'phones': all_phones}
    return render(request, template, context)


def show_product(request, slug):
    '''При запросе <имя_сайта>/catalog/iphone-x должна открываться страница
    с отображением информации по телефону.
    iphone-x — это для примера, это значние берётся из slug'''
    
    template = 'product.html'
    
    phone = Phone.objects.filter(slug__contains=slug).first()
    print(f'{phone=}')
    context = {'phone': phone}
    return render(request, template, context)
