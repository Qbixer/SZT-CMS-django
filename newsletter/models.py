from django.db import models
from .helpers import createRandomString,returnDateInFuture
from ckeditor.fields import RichTextField

# Create your models here.

class NewsletterUser(models.Model):
  email = models.EmailField(unique=True)
  activation_code = models.CharField(max_length=64, default=createRandomString)
  activated = models.BooleanField(default=False)
  expire_date = models.DateTimeField(default=returnDateInFuture)
  delete_code = models.CharField(max_length=64, default=createRandomString)
  

class MailConfiguration(models.Model):
  host = models.CharField(max_length=255)
  address = models.EmailField()
  password = models.CharField(max_length=255)

class EmailSent(models.Model):
  title = models.CharField(max_length=200, null=True, blank=True)
  body = RichTextField()

