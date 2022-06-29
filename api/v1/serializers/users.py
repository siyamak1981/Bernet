
from rest_framework import serializers 
from users.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()


#######################
### User Serializer ###
####################### 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
      
class UserSerializer(serializers.ModelSerializer):
    def get_profile(self, obj):
        return {
            "id":obj.profile.id,
            "phone":obj.profile.phone,
            "address":obj.profile.address,
            "zip":obj.profile.zip,
            "number":obj.profile.number,
        }
    profile = serializers.SerializerMethodField("get_profile")
    class Meta:
        model = User
        fields = "__all__"