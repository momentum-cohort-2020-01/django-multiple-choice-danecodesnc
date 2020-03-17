from django.forms import ModelForm
from .models import Deck
from django import forms
from .models import User, FlashCard, Deck

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model
    '''
    class Meta:
        model = Deck
        fields = ['title', 'description']

class CardForm(forms.ModelForm):

    class Meta:
        model = FlashCard
        fields = ['front', 'back', 'deck']