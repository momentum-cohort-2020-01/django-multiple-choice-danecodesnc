#This is our origional urls.py file that comes in our project.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from flashcards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
       
]