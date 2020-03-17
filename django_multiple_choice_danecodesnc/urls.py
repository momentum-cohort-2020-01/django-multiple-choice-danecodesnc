# This is our origional urls.py file that comes in our project.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from flashcards import views

urlpatterns = [
    
    path('', views.flashCard, name="home"),
    path('flashCard/new/', views.flashCard_new, name='flashcard_new'),
    # path('flashCard/<int:pk>/', views.flashCard_detail, name='flashcard_detail'),
    path('flashCard/<int:pk>/edit/', views.flashCard_edit, name='flashcard_edit'),
    path('flashCard/<int:pk>/delete/', views.flashCard_delete, name='flashcard_delete'), 
    # path('flashcard/', views.create_user, name="create_user"),
    path('admin/', admin.site.urls),


       
]
