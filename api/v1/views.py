from rest_framework import viewsets
from .serializers.users import UserSerializer
from users.models import Profile
from api.v1.serializers.users import ProfileSerializer
from django.contrib.auth import get_user_model
User = get_user_model()



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user'
    lookup_url_kwarg = 'user'