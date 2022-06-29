from django.urls import re_path,include
from rest_framework import routers
from api.v1.views import UserViewSet,CityViewSet, ProvinceViewSet
from dj_rest_auth.views import PasswordResetConfirmView

app_name = "api"
router = routers.DefaultRouter()
router.register(r'v1/users', UserViewSet)
router.register(r'v1/city', CityViewSet)
router.register(r'v1/province', ProvinceViewSet)




urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^v1/rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^v1/rest-auth/', include('dj_rest_auth.urls')),
    re_path(r'^v1/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path(r'^v1/rest-auth/password/reset/confirm/<uuid>/<token>/', PasswordResetConfirmView.as_view(), name = "password-reset-confirm")
] 
    # re_path(r'v1/users/profile/(?P<user>\d+)/$', APIRetrieveUpdateUserProfile.as_view(), name = 'user-profile'),
    # re_path(r"^users/", UserListView.as_view(), name = "user_list"),