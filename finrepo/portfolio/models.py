from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('portfolio:portfolio_list')


class PortfolioValue(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=16, decimal_places=2, default_currency='COP')
    added = MoneyField(max_digits=16, decimal_places=2, default_currency='COP', default=Money(0, 'COP'))
    date_added = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse_lazy('portfolio:portfolio_value_view', kwargs={'pk': self.portfolio_id})
