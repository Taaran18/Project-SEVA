from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class OrganizationUser(models.Model):
    
    class Meta:
        pass
