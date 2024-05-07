from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email', 'seller']
        
    def create(self, validated_data):
        print(validated_data)
        seller=validated_data.get('seller')
        user=User.objects.create_user(**validated_data)
        
        try:
            seller_group=Group.objects.get(name='seller')
            buyer_group=Group.objects.get(name='buyer')
        except Group.DoesNotExist:
            raise serializers.ValidationError("Group not found")
        if seller:
            user.groups.add(seller_group)
        else:
            user.groups.add(buyer_group)
        user.save()
        return user
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','seller']
        
        

    


