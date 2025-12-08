from argparse import Namespace
from django.contrib import admin
from django.urls import include, path

import main
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('main.urls', namespace='main'))
]
