from django import forms
from django.forms import DateInput

from .models import Portfolio, PortfolioValue


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'user']


class PortfolioValueForm(forms.ModelForm):
    class Meta:
        model = PortfolioValue
        fields = ["portfolio", 'balance', 'added', 'date_added']
        widgets = {
            'date_added': DateInput(attrs={'type': 'date'}),
        }
