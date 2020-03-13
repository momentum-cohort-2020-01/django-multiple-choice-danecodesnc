from django.forms import ModelForm
from .models import Deck
from django import forms
from .models import Post

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model
    '''
    class Meta:
        model = Deck
        fields = ['title', 'description']

class CardForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = ['front', 'back', 'deck']