from rest_framework import serializers
from app.models import Profile ,Users


      

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'
     
     
     
class UserProfileSerializers(serializers.ModelSerializer):
    user_data= ProfileSerializer(many=True ,read_only=True )
    class Meta:
        model = Users
        fields ='__all__'
        
   