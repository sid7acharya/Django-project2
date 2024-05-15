from django.shortcuts import render
from .models import OrderItem,Order
from .serializers import OrderItemSerializer, OrderCreateSerializer,OrderItemCreateSerializer,OrderSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateAPIView


# Create your views here.

class OrderView(ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
class OrderCreateView(CreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderCreateSerializer
    
class OrderUpdateView(UpdateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderDeleteView(DestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
    
class OrderItemListView(ListAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
    
class OrderItemCreateView(CreateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemCreateSerializer


class OrderItemUpdateView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
    
class OrderItemRetrieveView(RetrieveUpdateAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer
    
class OrderItemDeleteView(DestroyAPIView):
    queryset=OrderItem.objects.all()
    serializer_class=OrderItemSerializer



