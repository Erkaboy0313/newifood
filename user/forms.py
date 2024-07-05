from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_ckeditor_5.widgets import CKEditor5Widget
from meal.models import Meal
from vegetable.models import Vegetable
from fruit.models import Fruit
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class RegisterForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username','password1','password2','email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class MealForm(forms.ModelForm):
    image_file = forms.ImageField(label='Image of the meal')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.required = True
        self.fields["description"].required = False

        if self.instance:
            self.fields["image_file"].required = False

    class Meta:
        model = Meal
        fields = ("country","name","title","image_file","description","avarage_cost")
        widgets = {
                "text": CKEditor5Widget(
                    attrs={"class": "django_ckeditor_5"}, config_name="comment"
                )
        }
        labels = {
            'country': 'Select where this meal is prepared most, or select Any',
            'name': 'Name of the meal',
            'title': 'Title of your post',
            'description': 'Your post content',
            'avarage_cost': 'Avarage cost of this meal',
        }
    


class FruitForm(forms.ModelForm):
    image_file = forms.ImageField(label='Image of the Fruit')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.required = True
        self.fields["description"].required = False

        if self.instance:
            self.fields["image_file"].required = False

    class Meta:
        model = Fruit
        fields = ("country","type","name","title","image_file","description","avarage_cost")
        widgets = {
                "text": CKEditor5Widget(
                    attrs={"class": "django_ckeditor_5"}, config_name="comment"
                )
        }
        labels = {
            'country': 'Select where this fruit is related, or select Any',
            'type': 'Select one category which fits',
            'name': 'Name of the Fruit',
            'title': 'Title of your post',
            'description': 'Your post content',
            'avarage_cost': 'Avarage cost of this fruit',
        }

class VegetableForm(forms.ModelForm):
    image_file = forms.ImageField(label='Image of the Vegetable')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for key,value in self.fields.items():
            value.required = True
        self.fields["description"].required = False

        if self.instance:
            self.fields["image_file"].required = False
    class Meta:
        model = Vegetable
        fields = ("country","season","name","title","image_file","description","avarage_cost")
        widgets = {
                "text": CKEditor5Widget(
                    attrs={"class": "django_ckeditor_5"}, config_name="comment"
                )
        }
        labels = {
            'country': 'Select where this vegetable is related, or select Any',
            'season': 'Select one category which fits',
            'name': 'Name of the Vegetable',
            'title': 'Title of your post',
            'description': 'Your post content',
            'avarage_cost': 'Avarage cost of this vegetable',
        }

