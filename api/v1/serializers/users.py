
from rest_framework import serializers 
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts.models import City , Province

#######################
### User Serializer ###
####################### 
class UserSerializer(serializers.ModelSerializer):
    def get_city(self, obj):
        return {
            "id":obj.city.id,
            "title":obj.city.title,
          
        }
    city = serializers.SerializerMethodField("get_city")
    class Meta:
        model = User
        fields = "__all__"


#######################
### City Serializer ###
####################### 
class CitySerializer(serializers.ModelSerializer):
    def get_province(self, obj):
        return {
            "id":obj.province.id,
            "title":obj.province.title,
          
        }
    province = serializers.SerializerMethodField("get_province")
    class Meta:
        model = City
        fields = "__all__"


#######################
### Province Serializer ###
####################### 
class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = "__all__"