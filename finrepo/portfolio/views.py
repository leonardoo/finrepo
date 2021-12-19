from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from djmoney import settings
from djmoney.contrib.exchange.models import convert_money

from .forms import PortfolioForm, PortfolioValueForm
from .models import Portfolio, PortfolioValue


class PortfolioListView(ListView):
    model = Portfolio
    context_object_name = 'portfolio_list'
    queryset = Portfolio.objects.all().select_related('user')


class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortfolioForm


class PortfolioUpdateView(UpdateView):
    model = Portfolio
    form_class = PortfolioForm


class PortfolioValueListView(DetailView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'portfolio/portfolio_value_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_value_list'] = PortfolioValue.objects.filter(
            portfolio=self.object
        ).select_related('portfolio').order_by('-date_added')
        context['portfolio_value_list_json'] = [
            {
                'date_added': portfolio_value.date_added,
                'balance': convert_money(portfolio_value.balance, settings.DEFAULT_CURRENCY).amount,
                'added': convert_money(portfolio_value.added, settings.DEFAULT_CURRENCY).amount
            }
            for portfolio_value in context['portfolio_value_list']
        ]
        return context


class PortfolioValueCreateView(CreateView):
    model = PortfolioValue
    form_class = PortfolioValueForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PortfolioValueUpdateView(UpdateView):
    model = PortfolioValue
    form_class = PortfolioValueForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
