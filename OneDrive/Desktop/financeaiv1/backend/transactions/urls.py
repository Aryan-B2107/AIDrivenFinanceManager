from django.urls import path
from . import views, api_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/transactions/', api_views.TransactionList.as_view(), name='api-transactions'),
]
