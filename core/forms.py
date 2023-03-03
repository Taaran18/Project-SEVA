from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from .models import *
class DateInput(forms.DateInput):
    input_type = 'date'

class NormalUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('photo','first_name','last_name','email','mobile','password','password','domain','state','city','skills')


class OrganizationUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('photo','first_name','last_name','email','mobile','password','password','domain','organisation_name','designation')

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = ('title','short_description','salary','skill_requirements',
                  'openings','location','duration','job_type',
                  'apply_by','start_date','about_the_program','perks','who_can_apply',
                  )
        widgets = {
            'apply_by': DateInput(),
            'start_date': DateInput(),
        }
    
