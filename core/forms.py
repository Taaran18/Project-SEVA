from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import *


class DateInput(forms.DateInput):
    input_type = "date"


class NormalUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "photo",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "password1",
            "password2",
            "domain",
            "state",
            "city",
            "address",
            "skills",
        )


class OrganizationUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "photo",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "password1",
            "password2",
            "domain",
            "organisation_name",
            "address",
            "designation",
        )


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            "title",
            "short_description",
            "salary",
            "skill_requirements",
            "openings",
            "location",
            "duration",
            "job_type",
            "apply_by",
            "start_date",
            "about_the_program",
            "perks",
            "who_can_apply",
        )
        widgets = {
            "apply_by": DateInput(),
            "start_date": DateInput(),
        }
