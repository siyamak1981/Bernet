from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Province, User, City


admin.site.register(User)
admin.site.register(City)
admin.site.register(Province)
