from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Person, Hotels


# def rules(request):
#    return render(request, 'rules.html')
#
# def establishments(request):
#    return render(request, 'establishments.html')
def index(request):
    return render(request=request, template_name="base.html")


def hotels(request):
    hotels_list = [
        {"name": "Виктория Отель & Бизнес Центр", "address": "Проспект Победителей 59, 3.6 км до центра", "stars": 5},
        {"name": "Робинсон Сити", "address": "улица Зыбицкая, 4-2, 0.8 км до центра", "stars": 5},
        {"name": "БонОтель", "address": "Улица Притыцкого 2, 4.1 км до центра", "stars": 4}]
    context = {'hotel_list': hotels_list}
    return render(request, 'hotels.html', context=context)


def users(request):
    users_list = [
        {"name": "Максим", "age": 29, "comments": ["Мой новый пост!", "Отличный отель."]},
        {"name": "Наташа", "age": 33, "comments": ["Пристижно выглядит.", "Удивительно неплохо!"]},
        {"name": "Денис", "age": 22, "comments": ["Спасибо очень классно.", "Отдыхаю отлично."]},
        {"name": "Саша", "age": 45, "comments": ["Я недоволен.", "Очень плохо."]},
        {"name": "Таня", "age": 32, "comments": ["спасибо за обслуживание.", "Круто"]},
        {"name": "Ання", "age": 47, "comments": ["Мой пост!", "Мы отдахнули отлично."]},
        {"name": "Миша", "age": 23, "comments": ["Не очень.", " М-да!"]},
        {"name": "Сергей", "age": 19, "comments": ["Для бабушек сойдет.", "Плохо."]},
        {"name": "Фил", "age": 33, "comments": ["Класс.", "спасибо."]},
        {"name": "Дима", "age": 36, "comments": ["Мне нравится", "Еще раз приеду"]}
    ]

    context = {'users_list': users_list}

    return render(request=request, template_name="users.html", context=context, )


def persons(request):
    context = {'persons_list': Person.objects.all()}
    return render(request=request, template_name="persons.html", context=context, )


def comments(request):
    users_list = [
        {"name": "Максим", "age": 29, "comments": ["Мой новый пост!", "Отличный отель."]},
        {"name": "Наташа", "age": 33, "comments": ["Пристижно выглядит.", "Удивительно неплохо!"]},
        {"name": "Денис", "age": 22, "comments": ["Спасибо очень классно.", "Отдыхаю отлично."]},
        {"name": "Саша", "age": 45, "comments": ["Я недоволен.", "Очень плохо."]},
        {"name": "Таня", "age": 32, "comments": ["спасибо за обслуживание.", "Круто"]},
        {"name": "Ання", "age": 47, "comments": ["Мой пост!", "Мы отдахнули отлично."]},
        {"name": "Миша", "age": 23, "comments": ["Не очень.", " М-да!"]},
        {"name": "Сергей", "age": 19, "comments": ["Для бабушек сойдет.", "Плохо."]},
        {"name": "Фил", "age": 33, "comments": ["Класс.", "спасибо."]},
        {"name": "Дима", "age": 36, "comments": ["Мне нравится", "Еще раз приеду"]}
    ]
    context = {'users_list': users_list}
    return render(request=request, template_name="comments.html", context=context, )


def hotels_view(request):
    context = {'hotels_list_view': Hotels.objects.all()}

    return render(request=request, template_name="hotels_view.html", context=context, )
