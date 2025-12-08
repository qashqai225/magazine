from argparse import Namespace
from django.contrib import admin
from django.urls import include, path

import main
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls', namespace='main')),# вывод ссылок из main
    path("catalog/", include('goods.urls', namespace='catalog')),# вывод ссылок из goods
]
