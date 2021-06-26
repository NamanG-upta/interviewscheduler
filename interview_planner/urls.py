from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index),
    path('create_interview/', views.create_interview, name="create_iv")
]
