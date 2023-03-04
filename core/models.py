from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import json
from django.utils import timezone
from django.utils.timesince import timesince
from datetime import datetime, timedelta
DOMAINS = (
("Aerospace and Aviation Sector", "Aerospace and Aviation Sector"),
("Agriculture", "Agriculture"),
("Apparel Made-Ups &amp; Home Furnishing Sector", "Apparel Made-Ups &amp; Home Furnishing Sector"),
("Automotive Skills Development Council", "Automotive Skills Development Council"),
("Banking", "Banking"),
("Beauty &amp; Wellness Sector", "Beauty &amp; Wellness Sector"),
("BFSI Sector", "BFSI Sector"),
("Capital Goods", "Capital Goods"),
("Construction Skill Development Council", "Construction Skill Development Council"),
("Domestic Workers Sector", "Domestic Workers Sector"),
("Electronics Sector Skills Council", "Electronics Sector Skills Council"),
("Education and Edutech", "Education and Edutech"),
("Tourism and Hospitality", "Tourism and Hospitality"),
("Food Industry Capacity &amp; Skill Initiative", "Food Industry Capacity &amp; Skill Initiative"),
("Furniture &amp; Fittings", "Furniture &amp; Fittings"),
("Gem &amp; Jewellery", "Gem &amp; Jewellery"),
("Handicrafts and Carpet Sector", "Handicrafts and Carpet Sector"),
("Healthcare Sector", "Healthcare Sector"),
("Hydrocarbon Sector", "Hydrocarbon Sector"),
("Indian Iron and Steel Sector", "Indian Iron and Steel Sector"),
("Indian Plumbing Skills council", "Indian Plumbing Skills council"),
("Infrastructure Equipment", "Infrastructure Equipment"),
("IT-ITeS Sector", "IT-ITeS Sector"),
("Leather Sector", "Leather Sector"),
("Life Sciences Sector Skill Development Council", "Life Sciences Sector Skill Development Council"),
("Logistics Sector", "Logistics Sector"),
("Management &amp; Entrepreneurship and Professional Skills Council (MEPSC)", "Management &amp; Entrepreneurship and Professional Skills Council (MEPSC)"),
("Media &amp; Entertainment", "Media &amp; Entertainment"),
("Paints and Coatings", "Paints and Coatings"),
("Power Sector", "Power Sector"),
("Retailers Association's", "Retailers Association's"),
("Rubber Skill Development Council", "Rubber Skill Development Council"),
("Green Jobs", "Green Jobs"),
("Mining Sector", "Mining Sector"),
("Persons with Disability", "Persons with Disability"),
("Sports, Physical Education, Fitness &amp; Leisure Skills Council", "Sports, Physical Education, Fitness &amp; Leisure Skills Council"),
("Telecom Sector ", "Telecom Sector "),
("Textile Sector", "Textile Sector"),
("Tourism and Hospitality", "Tourism and Hospitality"),
("other", "other"),
)

USER_TYPE = (
             ('organisation','organisation'),
             ('normal','normal'),
             )

JOB_TYPE = (
            ('Part-Time','Part-Time'),
            ('Full-Time','Full-Time'),
            )
class User(AbstractUser):
    mobile = models.BigIntegerField(name='mobile',null=True)
    domain = models.CharField(choices=DOMAINS,max_length=255,null=True) 
    user_type = models.CharField(choices=USER_TYPE, max_length=50,null=True)
    photo = models.ImageField(name='photo',upload_to='images',null=True,blank=True)
    about = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255)
    ## User Fields
    user_state = models.CharField(name="state",max_length=60,null=True)
    user_city = models.CharField(name="city", max_length=60,null=True)
    user_skills = models.TextField(name="skills", help_text='Enter your skills separated by comma: skill1, skill2')
    user_dob = models.DateField(null=True)
    ## Organisation Fields
    organisation_name = models.CharField(name="organisation_name",max_length=200,null=True) 
    organisation_designation = models.CharField(name="designation", max_length=150,null=True)
    def get_skills(self):
        return list(map(lambda x:x.strip(),list(self.skills.split(','))))
    def __str__(self):
        return self.first_name
    def save(self, *args, **kwargs):
    
        self.username = self.email
        super(User, self).save(*args, **kwargs)
    def is_organisation(self):
        return self.user_type=="organisation"
    def is_normal(self):
        return self.user_type=="normal"
    def get_age(self):
        if self.user_type == "normal" and self.user_dob:
            return timesince(self.user_dob, datetime.now())
        return ''
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=155)
    company = models.ForeignKey(to=User, limit_choices_to={'user_type':'organisation'}, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=255)
    about_the_program = models.TextField()
    perks = models.TextField()
    who_can_apply = models.TextField()
    salary = models.CharField(max_length=50)
    skill_requirements = models.CharField(max_length=255)
    openings = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=80)
    job_type = models.CharField(choices=JOB_TYPE,max_length=155)
    apply_by = models.DateField()
    start_date = models.DateField()
    applicants = models.ManyToManyField(User,limit_choices_to={'user_type':'normal'},related_name='posted_by', null=True, blank=True)




class Education(models.Model):
    user = models.ForeignKey(User,limit_choices_to={'user_type':'is_normal'},on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    from_year = models.PositiveIntegerField()
    to_year = models.PositiveIntegerField()

class Work(models.Model):
    user = models.ForeignKey(User,limit_choices_to={'user_type':'is_normal'},on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    desc = models.CharField(max_length=255)
    from_year = models.PositiveIntegerField()
    to_year = models.PositiveIntegerField()


    
