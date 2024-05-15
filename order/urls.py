from django.urls import path
from .views import OrderView,OrderCreateView,OrderUpdateView,OrderDeleteView,OrderRetrieveView,OrderItemCreateView,OrderItemUpdateView,OrderItemRetrieveView,OrderItemDeleteView,OrderItemListView

urlpatterns = [
    path("",OrderView.as_view(),name='order-list'),
    path("create/",OrderCreateView.as_view(),name='order-create'),
    path("<int:pk>/update/",OrderUpdateView.as_view(),name='order-update'),
    path("<int:pk>/delete/",OrderDeleteView.as_view(),name='order-delete'),
    path("<int:pk>/retrieve/",OrderRetrieveView.as_view(),name='order-retrieve'),
    path("",OrderItemListView.as_view(),name='order-view'),
    path("orderitem/create/",OrderItemCreateView.as_view(),name='orderitem-create'),
    path("orderitem/<int:pk>/update/",OrderItemUpdateView.as_view(),name='orderitem-udate'),
    path("orderitem/<int:pk>/delete/",OrderItemDeleteView.as_view(),name='orderitem-delete'),
    path("orderitem/<int:pk>/retrieve/",OrderItemRetrieveView.as_view(),name='orderitem-retrieve')
    
]
