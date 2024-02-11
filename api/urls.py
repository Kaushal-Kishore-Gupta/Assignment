from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('find_largest/',find_largest.as_view(),name='find_largest'),
]
