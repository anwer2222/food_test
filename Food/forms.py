# myproject/Food/forms.py

from django import forms
from .models import Pizza, Burger

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name', 'ingredients', 'price']

class BurgerForm(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ['name', 'ingredients', 'price']