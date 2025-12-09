from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


# база для "головної сторінки"
def index(request):
    
    categories=Categories.objects.all()
    context = {
        "title": "Головна Сторінка",
        "content": "Магазин меблів для HOME",
        "categories": categories
    }

    return render(request, "main/index.html", context)


# база для сторінки "про нас"
def about(request):
    context = {
        "title": "Сторінка про нас",
        "content": "Про Нас",
        "text_on_page": "Все що потрібно ви взнаєте тут",
    }

    return render(request, "main/about.html", context)

# база для сторінки "Контактна інформація"
def contakt(request):
    context = {
        "title": "Контактна інформація",
        "content": "Контактна інформація",
        "text_on_page": "Все що потрібно ви взнаєте тут Контактна інформація",
    }

    return render(request, "main/contakt.html", context)


# Create your views here.
