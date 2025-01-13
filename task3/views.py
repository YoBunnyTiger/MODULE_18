from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    items = {
        'item1': 'DOOM',
        'item2': 'ГЭГ: Отвязное приключение',
        'item3': 'БРАТЬЯ ПИЛОТЫ'
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
