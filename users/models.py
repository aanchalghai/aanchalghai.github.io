from django.db import models
from django.contrib import auth
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

# Create your models here.

class PersonalInfo(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER,null=True)
    phone = models.CharField(max_length=11,null=True,unique = True)
    address = models.TextField(unique=True,null=True)
    date_of_birth = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        PersonalInfo.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    instance.personalinfo.save()

def user_directory_path(instance, filename):
    user = instance.user.first_name
    return '{0}/{1}/'.format(user, filename)

class Listings(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=20, primary_key = True)
    CATEGORY = (
        ('R', 'Rent'),
        ('S', 'Sale'),
    )
    category = models.CharField(max_length=1, choices=CATEGORY,null=True)
    price = models.CharField(max_length=10, null=True)
    bedrooms = models.CharField(max_length=2, null=True)
    bathrooms = models.CharField(max_length=2, null=True)
    area = models.CharField(max_length=4, null=True)
    locality = models.CharField(max_length=10, null=True)
    city = models.CharField(max_length=20,blank = True, null=True)
    state = models.CharField(max_length=10,blank = True, null=True)
    country = models.CharField(max_length=10,blank = True, null=True)
    pin_code = models.CharField(max_length=10,blank = True, null=True)
    description = models.TextField(blank = True, null = True, unique = True)
    pictures = models.ImageField(null = False, blank = True,upload_to=user_directory_path)

    def __str__(self):
        return self.user.username
