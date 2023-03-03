from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import *
from django.contrib.auth import get_user_model


class WorkInline(admin.TabularInline):
    model = Work
    min_num = 3
    max_num = 20
    extra = 1



class EducationInline(admin.TabularInline):
    model = Education
    min_num = 3
    max_num = 20
    extra = 1



class CustomUserAdmin(UserAdmin):
    '''
        Admin View for CustomUser
    '''
    model = get_user_model()
    list_display = ('name', 'user_type')
    list_filter = ('user_type',)
    inlines = [
        WorkInline, EducationInline
    ]
    

    def name(self):
        return self.first_name + ' '+self.last_name


admin.site.register(get_user_model(), CustomUserAdmin)

admin.register(settings.AUTH_USER_MODEL, UserAdmin)


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)
