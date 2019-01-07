from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class ContentType(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class Section(models.Model):
    title = models.CharField(max_length=50, unique=False, help_text="Required. Maximum 50 characters.", blank=False)
    tab_title = models.CharField(max_length=50, unique=False, null=True, help_text="Optional. Maximum 50 characters.", blank=True)
    url = models.CharField(max_length=255, unique=False, null=False, help_text="Required. Maximum 250 characters use only letter, numbers and \'_\' sign.",validators=[RegexValidator(regex=r'^[a-zA-Z0-9_]{1,250}$',message='Use only letters, numbers and \'_\' sign.',code='invalid_url')], blank=False)
    hidden = models.BooleanField(default=False, null=False, help_text="Should page be hidden for now.", blank=False)
    should_display = models.BooleanField(default=True, help_text="Optional. Should page be displayed.", blank=False)
    deleted = models.BooleanField(default=False, help_text="Should page be marked as deleted. Possible to undo in admin panel.", blank=False)
    order_number = models.IntegerField(default = 0, help_text="Smaller number => More to the left. Sections sort ascending.", blank=False)
    restricted = models.BooleanField(default=False, help_text="Should page restricted for logged people.", blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.title

class PageLayout(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)



class Custom_HTML(models.Model):
    url = models.CharField(max_length=255, unique=True)
    html = models.CharField(max_length=10000)

