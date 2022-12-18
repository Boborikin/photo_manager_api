from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.postgres.fields import JSONField

class Photo(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    picture = models.ImageField(upload_to='pictures/')
    description = models.CharField(max_length=200)
    people_list = JSONField()
    upload_date = models.DateTimeField(default=timezone.now)
    geolocation = models.CharField(max_length=200)

