# api/urls.py
from django.urls import path

from .views import OrderListView, AccessListView, \
    SubscriptionListView, EndpointListView
from .views import OrderDetailView, AccessDetailView, Option82DetailView, \
    DhcplookupListView

urlpatterns = [
    path('', EndpointListView.as_view()),
    path('accesses', AccessListView.as_view()),
    path('orders', OrderListView.as_view()),
    path('subscriptions', SubscriptionListView.as_view()),
    path('accesses/<uuid:pk>/', AccessDetailView.as_view()),
    path('orders/<uuid:pk>/', OrderDetailView.as_view()),
    path('option82/<pk>/', Option82DetailView.as_view()),
    path('dhcplookup', DhcplookupListView.as_view()),
]