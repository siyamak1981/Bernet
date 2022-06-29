from django.urls import re_path,include
from rest_framework import routers
from api.v1.views import UserViewSet,ProfileViewSet


app_name = "api"
router = routers.DefaultRouter()
router.register(r'v1/users', UserViewSet)
router.register(r'v1/profile', ProfileViewSet)




urlpatterns = [
    re_path(r'^', include(router.urls)),
    # re_path(r'v1/users/profile/(?P<user>\d+)/$', APIRetrieveUpdateUserProfile.as_view(), name = 'user-profile'),
    # re_path(r"^users/", UserListView.as_view(), name = "user_list"),
] 