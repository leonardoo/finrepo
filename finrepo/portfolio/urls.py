from django.urls import path

from .views import (
    PortfolioCreateView,
    PortfolioListView, PortfolioUpdateView, PortfolioValueListView, PortfolioValueCreateView, PortfolioValueUpdateView
)

app_name = "portfolio"

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio_list'),
    path('create/', PortfolioCreateView.as_view(), name='portfolio_create'),
    path('update/<int:pk>/', PortfolioUpdateView.as_view(), name='portfolio_update'),
    path('<int:pk>/value/', PortfolioValueListView.as_view(), name='portfolio_value_view'),
    path('value/create/', PortfolioValueCreateView.as_view(), name='portfolio_value_create'),
    path('value/update/<int:pk>/', PortfolioValueUpdateView.as_view(), name='portfolio_value_update'),
]

