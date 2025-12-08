from django.shortcuts import render


# база для "головної сторінки"
def index(request):
    context = {
        "title": "Головна Сторінка",
        "content": "Магазин меблів для HOME",
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


# Create your views here.
