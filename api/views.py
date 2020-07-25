# api/views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from accesses.models import Accesses
from orders.models import Orders
from subscriptions.models import Subscriptions
from endpoints.models import Endpoints
from option82.models import Option82
from dhcplookup.models import Dhcplookup
from .serializers import AccessListSerializer, OrderListSerializer, \
    SubscriptionListSerializer, EndpointListSerializer
from .serializers import AccessDetailSerializer, OrderDetailSerializer, \
    Option82DetailSerializer, DhcplookupListSerializer


class AccessListView(generics.ListAPIView):
    queryset = Accesses.objects.all()
    serializer_class = AccessListSerializer


class AccessDetailView(generics.RetrieveAPIView):
    queryset = Accesses.objects.all()
    serializer_class = AccessDetailSerializer


class OrderListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderListSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderDetailSerializer


class SubscriptionListView(generics.ListAPIView):
    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionListSerializer


class EndpointListView(generics.ListAPIView):
    queryset = Endpoints.objects.all()
    serializer_class = EndpointListSerializer


class Option82DetailView(generics.RetrieveAPIView):
    queryset = Option82.objects.all()
    serializer_class = Option82DetailSerializer


class DhcplookupListView(generics.ListAPIView):
    queryset = Dhcplookup.objects.all()
    serializer_class = DhcplookupListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('__all__')

