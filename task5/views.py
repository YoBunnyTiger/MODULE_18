from django.shortcuts import render, HttpResponse
from .forms import UserRegister


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    page_name = 'Форма регистрации'
    info = {}
    initial_data = {
        'username': '',
        'age': '',
    }

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            repeat_password = form.cleaned_data.get('repeat_password')
            age = form.cleaned_data.get('age')

            initial_data = {
                'username': username,
                'age': age
            }

            errors = {}
            if username in users:
                errors['username'] = 'Пользователь уже существует'
            if password != repeat_password:
                errors['repeat_password'] = 'Пароли не совпадают'
            if int(age) < 18:
                errors['age'] = 'Вы должны быть старше 18'
            if errors:
                info['error'] = errors
            else:
                users.append(username)
                return HttpResponse(f"Приветствуем, {username}!")

    else:
        form = UserRegister(initial=initial_data)

    info['form'] = form

    context = {
        'page_name': page_name,
        'initial_data': initial_data,
        'info': info
    }
    print('django_sign_up')
    return render(request, "fifth_task/registration_page.html", context)


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    page_name = 'Форма регистрации'
    info = {}
    initial_data = {
        'username': '',
        'age': '',
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        initial_data = {
            'username': username,
            'age': age
        }

        errors = {}
        if username in users:
            errors['username'] = 'Пользователь уже существует'
        if password != repeat_password:
            errors['repeat_password'] = 'Пароли не совпадают'
        if int(age) < 18:
            errors['age'] = 'Вы должны быть старше 18'
        if errors:
            info['error'] = errors
        else:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}!")

    context = {
        'page_name': page_name,
        'initial_data': initial_data,
        'info': info
    }
    return render(request, "fifth_task/registration_page.html", context)
