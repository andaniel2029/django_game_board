from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Enthusiast, CollectionItem


class EnthusiastCreationForm(UserCreationForm):

    class Meta:
        model = Enthusiast
        fields = ["username", "email", "password1", "password2", "country", "city", "avatar"]


class CollectionItemForm(ModelForm):

    class Meta:
        model = CollectionItem
        exclude = ["enthusiast", "game"]

#TODO: Check with Scott

class CollectionItemImageForm(ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = CollectionItem
        fields = ('image',)
