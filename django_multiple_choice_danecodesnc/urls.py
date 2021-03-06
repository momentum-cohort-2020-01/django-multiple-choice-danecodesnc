# This is our origional urls.py file that comes in our project.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from flashcards import views

urlpatterns = [
    
    path('', views.homepage, name="home"),
    path('flashcard/add_deck/', views.create_deck, name='add-deck'),
    path('flashcard/deck_detail/<int:pk>/', views.deck_detail, name='deck-detail'),
    path('flashcard/<int:pk>/delete/', views.deck_delete, name='deck-delete'), 
    path('flashcard/new/', views.flashcard_new, name='flashcard_new'),
    path('flashcard/<int:pk>/', views.flashcard, name='flashcard'),
    path('flashcard/<int:pk>/edit/', views.flashcard_edit, name='flashcard_edit'),
    path('flashcard/<int:pk>/delete/', views.flashcard_delete, name='flashcard_delete'), 
    # path('flashcard/', views.create_user, name="create_user"),
    path('admin/', admin.site.urls),


       
]
