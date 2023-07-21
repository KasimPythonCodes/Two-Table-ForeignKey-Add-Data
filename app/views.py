from django.shortcuts import render ,HttpResponse
from rest_framework import serializers ,response , generics
from rest_framework.viewsets import ModelViewSet
from app.models import Profile ,Users
from app.serializers import UserProfileSerializers ,ProfileSerializer
from django.contrib.auth.hashers import make_password
import json
# Create your views here.


class UserRegistrationapi(ModelViewSet):
    queryset=Users.objects.all()
    serializer_class=UserProfileSerializers 
    
class Profiledataapi(ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer     

"""
class UserProfile(generics.GenericAPIView):
    serializer_class = UserProfileSerializers
    
    queryset = Users.objects.all()
    def get(self , request):
        stu =Users.objects.all()
        serializer = self.serializer_class(stu, many=True)
        return response.Response(serializer.data)
    
    def post(self , request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_pic =serializer.data.get('user_pic')
        fullname =serializer.data.get('fullname')
        phone_no =serializer.data.get('phone_no')
        email =serializer.data.get('email')
        password =serializer.data.get('password')
        
        print(user_pic , fullname ,phone_no ,email , password)
        if Users.objects.filter(email=email).exists() :
            raise serializers.ValidationError("Email already exists")
        elif Users.objects.filter(phone_no=phone_no).exists():
            raise serializers.ValidationError("Phone Number already exists")
        else:
            user_obj = Users.objects.create(
            fullname=fullname ,
            phone_no=phone_no ,
            email=email ,
            password=make_password(password)
            )
            user_obj.save()
            Profile.objects.create(user=user_obj , user_pic=user_pic).save()
            return response.Response(serializer.data)

"""           
        
        
        
