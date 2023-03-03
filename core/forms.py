from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import *
class NormalUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('photo','first_name','last_name','email','mobile','password','password','domain','state','city','skills')


class OrganizationUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('photo','first_name','last_name','email','mobile','password','password','domain','organisation_name','designation')

