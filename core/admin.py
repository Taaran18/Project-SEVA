from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import *
from django.contrib.auth import get_user_model


class WorkInline(admin.TabularInline):
    model = Work
    min_num = 0
    max_num = 20
    extra = 1



class EducationInline(admin.TabularInline):
    model = Education
    min_num = 0
    max_num = 20
    extra = 1



class CustomUserAdmin(UserAdmin):
    '''
        Admin View for CustomUser
    '''
    model = get_user_model()
    list_display = ('first_name', 'user_type')
    list_filter = ('user_type',)
    fieldsets = (
        (None, {'fields': ('email', 'password','user_type','photo')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Other info', {'fields': ('about','mobile','skills','user_dob')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        )
        
    add_fieldsets = (
                    ('Personal Information',{
                     'fields': ('username','email','mobile','user_type','password1','password2')
                      }
                    ),
                )
    
    def get_inlines(self, request, obj=None):
        if obj and obj.user_type!="organisation":
            return [
             WorkInline, EducationInline
            ]
        else:
            return []
    
  
    def name(self,obj):
        return (obj.first_name + ' '+obj.last_name)


admin.site.register(get_user_model(), CustomUserAdmin)

admin.register(settings.AUTH_USER_MODEL, UserAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('id','title')


admin.site.register(Job, JobAdmin)
