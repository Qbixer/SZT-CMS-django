from django.db import models
from .helpers import createRandomString,returnDateInFuture

# Create your models here.

class NewsletterUser(models.Model):
  email = models.EmailField()
  activation_code = models.CharField(max_length=64, default=createRandomString)
  activated = models.BooleanField(default=False)
  expire_date = models.DateTimeField(default=returnDateInFuture)
  delete_code = models.CharField(max_length=64, default=createRandomString)

class MailConfiguration(models.Model):
  host = models.CharField(max_length=255)
  address = models.EmailField()
