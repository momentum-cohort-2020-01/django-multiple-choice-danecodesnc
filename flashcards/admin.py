#This is part of our app.
from django.contrib import admin
from .models import FlashCard, Deck

admin.site.register(FlashCard)
admin.site.register(Deck)

# Register your models here.
