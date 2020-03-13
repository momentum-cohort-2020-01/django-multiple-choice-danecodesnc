# This is part of our app.
from django.db import models
from users.models import User


class FlashCard(models.Model):
    front = models.CharField(blank=True, null=True, max_length=100)
    back = models.CharField(blank=True, null=True, max_length=100)
    deck = models.ForeignKey(
        'Deck', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.front}'


class Deck(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=False, blank=True)
    slug = models.SlugField(null=False, unique=True)
   
    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)    
    




   
# question = models.CharField(max_length=200)
#     answer = models.CharField(max_length=200)


