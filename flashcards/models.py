# This is part of our app.
from django.db import models
from users.models import User


class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=False, blank=True)
   
    def __str__(self):
        return f'{self.title}'
    

class FlashCard(models.Model):
    front = models.CharField(blank=True, null=True, max_length=100)
    back = models.CharField(blank=True, null=True, max_length=100)
    deck = models.ForeignKey(
        'Deck', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.front}'



   
# question = models.CharField(max_length=200)
#     answer = models.CharField(max_length=200)


