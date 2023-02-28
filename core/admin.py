from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
admin.register(settings.AUTH_USER_MODEL, UserAdmin)
