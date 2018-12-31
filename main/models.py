from django.db import models

# Create your models here.

class ContentType(models.Model):
    name = models.CharField(max_length=255,unique=True)

class Section(models.Model):
    title = models.CharField(max_length=50, unique=True)
    browser_title = models.CharField(max_length=50, unique=False)
    url = models.CharField(max_length=255, unique=True, null=True)
    hidden = models.BooleanField(default=False)
    content = models.CharField(max_length=10000)
    should_display = models.BooleanField(default=True)
    contentType = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    

class Subsection(models.Model):
    parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=False)
    browser_title = models.CharField(max_length=50, unique=False)
    url = models.CharField(max_length=255, unique=False)
    hidden = models.BooleanField(default=False)
    content = models.CharField(max_length=10000)
    contentType = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)


class Custom_HTML(models.Model):
    url = models.CharField(max_length=255, unique=True)
    html = models.CharField(max_length=10000)

