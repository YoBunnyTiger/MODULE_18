from django.shortcuts import render


def index(request):
    title = 'Главная страница'
    text = 'Магазин'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'third_task/platform.html', context)


def shop(request):
    title = 'Игры 90-х'
    items = {
        'item1': 'DOOM',
        'item2': 'ГЭГ: Отвязное приключение',
        'item3': 'БРАТЬЯ ПИЛОТЫ'
    }
    context = {
        'title': title,
        'items': items,
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    text = 'Здесь будет информация о ваших товарах.'
    context = {
        'text': text,
    }
    return render(request, 'third_task/cart.html', context)
