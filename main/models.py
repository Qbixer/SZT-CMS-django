from django.db import models

# Create your models here.

class Section(models.Model):
    title = models.CharField(max_length=50, unique=True)
    browser_title = models.CharField(max_length=50, unique=False)
    url = models.CharField(max_length=255, unique=True)
    hidden = models.BooleanField(default=False)
    content = models.CharField(max_length=10000)
    should_display = models.BooleanField(default=True)

class Subsection(models.Model):
    parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    browser_title = models.CharField(max_length=50, unique=False)
    url = models.CharField(max_length=255, unique=True)
    hidden = models.BooleanField(default=False)
    content = models.CharField(max_length=10000)
    should_display = models.BooleanField(default=True)


class Subsubsection(models.Model):
    parent = models.ForeignKey(Subsection, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    browser_title = models.CharField(max_length=50, unique=False)
    url = models.CharField(max_length=255, unique=True)
    hidden = models.BooleanField(default=False)
    content = models.CharField(max_length=10000)
    should_display = models.BooleanField(default=True)
    

class Custom_HTML(models.Model):
    url = models.CharField(max_length=255, unique=True)
    html = models.CharField(max_length=10000)

