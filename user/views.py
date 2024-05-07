from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserCreateSerializer,UserListSerializer
from .models import User

# Create your views here.

def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    
    return{
        'refresh':str(refresh),
        'access':str(refresh.access_token),
    }
    
class UserCreateView(CreateAPIView):
    serializer_class=UserCreateSerializer
    queryset=User.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        
        token=get_tokens_for_user(user)
        
        return Response({'token':token,'msg':'Signup Successful'}, status=status.HTTP_201_CREATED)
    
class SellerListView(ListAPIView):
        
        serializer_class= UserListSerializer
        
        def get_queryset(self):
            
            return User.objects.all()
        
class UserListView(ListAPIView):
    
        serializer_class=UserListSerializer
        
        def get_queryset(self):
                
            return User.objects.all()
        
class BuyerListView(ListAPIView):
    
        serializer_class=UserListSerializer
        
        def get_queryset(self):
                
            return User.objects.filter()
        
       
class UserUpdateView(UpdateAPIView):
    
        serializer_class=UserListSerializer
        
        def get_queryset(self):
                
            return User.objects.all()
        

class UserDeleteView(DestroyAPIView):
    
        serializer_class=UserListSerializer
        
        def get_queryset(self):
                
            return User.objects.all()
        
      
class UserRetrieveView(RetrieveAPIView):
    
        serializer_class=UserListSerializer
        
        def get_queryset(self):
                
            return User.objects.all()
        

        

        
        
        
        