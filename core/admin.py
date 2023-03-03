from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.conf import settings
from .models import *

class WorkInline(admin.TabularInline):
        '''
            Tabular Inline View for Work
        '''
      model = Work
      min_num = 3
      max_num = 20
      extra = 1
      raw_id_fields = (,)

class EducationInline(admin.TabularInline):
        '''
            Tabular Inline View for Education
        '''
      model = Education
      min_num = 3
      max_num = 20
      extra = 1
      raw_id_fields = (,)

class CustomUserAdmin(UserAdmin):
    '''
        Admin View for CustomUser
    '''
    list_display = ('name','user_type')
    list_filter = ('user_type')
    inlines = [
        WorkInline, EducationInline
    ]
    raw_id_fields = ('',)
    readonly_fields = ('',)
    search_fields = ('',)
    def name(self):
        return self.first_name+ ' '+self.last_name
admin.site.register(CustomUser, CustomUserAdmin)

admin.register(settings.AUTH_USER_MODEL, UserAdmin)


class JobAdmin(admin.ModelAdmin):
    pass


admin.site.register(Job, JobAdmin)

