from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    pass














#I'm going to type out Clinton's example right here for the user.model.py. 
# I was a little confused as to what this does until class today March 10.
# Pipenv install django registration
#This will get django registration started https://django-registration.readthedocs.io/en/3.1/quickstart.html
#There is a bit of work to be done, involving creating templates and so on, so be aware if you decide to do this.
#Instead we are installing django registration-redux.
#This can be installed by doing pipenv install registraiton-redux in your terminal.







# User
# Name
# Password
# Redux? (Registration-redux which can be installed)

# class Deck(models.Model):
#     pass

# Deck
# Title
# Description

# class FlashCards(models.Model)
#     pass

# FlashCards
# Words
# definitions


# class Results(models.Model)
#     pass

# Results


