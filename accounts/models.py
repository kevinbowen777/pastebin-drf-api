from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class CustomUser(AbstractUser):
    name = models.CharField("Name of User", blank=True, max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField("Bio", blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", blank=True)
    country = CountryField("Country", blank=True)

    def __str__(self):
        return self.username
