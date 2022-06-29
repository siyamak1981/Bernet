from rest_framework import viewsets
from .serializers.users import UserSerializer,ProvinceSerializer, CitySerializer
from accounts.models import City , Province
from django.contrib.auth import get_user_model
User = get_user_model()
from api.permissions import IsSuperUserOrStaffReadOnly

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = (IsSuperUserOrStaffReadOnly,)



class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = (IsSuperUserOrStaffReadOnly,)



class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    permission_classes = (IsSuperUserOrStaffReadOnly,)