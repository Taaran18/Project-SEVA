from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
from django.conf import settings
DOMAINS = (
("All", "All"),
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
)
class User(AbstractUser):
    mobile = models.BigIntegerField(name='mobile')
    domain = models.CharField(choices=DOMAINS,max_length=255) 

    ## User Fields
    user_state = models.CharField(max_length=60,null=True)
    user_city = models.CharField(max_length=60,null=True)
    user_skills = models.TextField(help_text='Enter your skills separated by comma: skill1, skill2')
    
    ## Organisation Fields
    organisation_name = models.CharField(max_length=200,null=True) 
    organisation_designation = models.CharField(max_length=150,null=True)


