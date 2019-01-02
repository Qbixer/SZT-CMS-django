from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class ContentType(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Section(models.Model):
    title = models.CharField(max_length=50, unique=False, help_text="Required. Maximum 50 characters.")
    tab_title = models.CharField(max_length=50, unique=False, null=True, help_text="Optional. Maximum 50 characters.")
    url = models.CharField(max_length=255, unique=False, null=False, help_text="Required. Maximum 250 characters use only letter, numbers and \'_\' sign.",validators=[RegexValidator(regex=r'^[a-zA-Z0-9_]{1,250}$',message='Use only letters, numbers and \'_\' sign.',code='invalid_url')])
    hidden = models.BooleanField(default=False, null=False, help_text="Should page be hidden for now.")
    content = models.CharField(max_length=10000, null=True, help_text="Optional. Maximum 10000 characters.")
    should_display = models.BooleanField(default=True, help_text="Optional. Should page be displayed.")
    contentType = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True, blank=True, help_text="Optional. How the page should be displayed.")
    deleted = models.BooleanField(default=False, help_text="Should page be marked as deleted. Possible to undo in admin panel.")
    order_number = models.IntegerField(default = 0, help_text="Smaller number => More to the left. Sections sort ascending.")



class Subsection(models.Model):
    parent = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=False)
    tab_title = models.CharField(max_length=50, unique=False)
    url = models.CharField(max_length=255, unique=False)
    hidden = models.BooleanField(default=False)
    content = models.CharField(max_length=10000)
    contentType = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    order_number = models.IntegerField(default = 0)



class Custom_HTML(models.Model):
    url = models.CharField(max_length=255, unique=True)
    html = models.CharField(max_length=10000)

