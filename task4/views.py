from django.shortcuts import render


def index(request):
    title = 'Главная страница'
    text = 'Магазин'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/platform.html', context)


def shop(request):
    title = 'Игры 90-х'
    games = [
        'DOOM',
        'ГЭГ: Отвязное приключение',
        'БРАТЬЯ ПИЛОТЫ'
    ]
    context = {
        'title': title,
        'games': games,
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    title = 'Корзина'
    text = 'Извинитеб ваша корзина пуста.'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/cart.html', context)
