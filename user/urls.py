from django.urls import path
from .views import UserCreateView,SellerListView,UserListView,BuyerListView,UserUpdateView,UserDeleteView,UserRetrieveView


urlpatterns = [
    path('create/',UserCreateView.as_view(),name='create-user'),
    path('list/',UserListView.as_view(),name='list-user'),
    path('buyer/',BuyerListView.as_view(),name='buyers'),
    path('seller/',SellerListView.as_view(),name="Seller"),
    path('user/',UserUpdateView.as_view(),name='update-user'),
    path('user/',UserDeleteView.as_view(),name='user-delete'),
    path('user/',UserRetrieveView.as_view(),name='user-retrieve')
]
