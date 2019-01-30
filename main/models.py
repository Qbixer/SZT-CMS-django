from django.db import models
from django.core.validators import RegexValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class ContentType(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return self.name

class MailConfiguration(models.Model):
  host = models.CharField(max_length=255)
  address = models.EmailField()
  password = models.CharField(max_length=255)

class EmailTemplate(models.Model):
    email_type = models.CharField(max_length=255,null=False,blank=False,unique=True)
    subject = models.CharField(max_length=500,null=False,blank=False)
    body = RichTextField()
    helper_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.email_type

class Section(models.Model):
    title = models.CharField(max_length=50, unique=False, help_text="Required. Maximum 50 characters.", blank=False)
    tab_title = models.CharField(max_length=50, unique=False, null=True, help_text="Optional. Maximum 50 characters.", blank=True)
    url = models.CharField(max_length=255, unique=False, null=False, help_text="Required. Maximum 250 characters use only letter, numbers and \'_\' sign.",validators=[RegexValidator(regex=r'^[a-zA-Z0-9_]{1,250}$',message='Use only letters, numbers and \'_\' sign.',code='invalid_url')], blank=False)
    hidden = models.BooleanField(default=False, null=False, help_text="Should page be hidden for now.", blank=False)
    should_display = models.BooleanField(default=True, help_text="Optional. Should page be displayed.", blank=False)
    deleted = models.BooleanField(default=False, help_text="Should page be marked as deleted. Possible to undo in admin panel.", blank=False)
    order_number = models.IntegerField(default = 0, help_text="Smaller number => More to the left. Sections sort ascending.", blank=False)
    restricted = models.BooleanField(default=False, help_text="Should page restricted for logged people.", blank=False)
    background_color = models.CharField(max_length=7, unique=False, default="#FFFFFF", help_text="Background color of the section page")
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)    
    def __str__(self):
        return self.title

class HomePage(models.Model):
    title = models.CharField(max_length=50, unique=False, help_text="Required. Maximum 50 characters.", blank=False)
    tab_title = models.CharField(max_length=50, unique=False, null=True, help_text="Optional. Maximum 50 characters.", blank=True)
    background_color = models.CharField(max_length=7, unique=False, default="#FFFFFF", help_text="Background color of the section page")
    background_color_theme = models.CharField(max_length=7, unique=False, default="#FFFFFF", help_text="Background color of the whole page")
    def __str__(self):
        return self.title

class PageLayout(models.Model):
    home_page = models.ForeignKey(HomePage, null=True, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, null=True, blank=True)
    order_number = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return self.title

class Post(models.Model):
    parent = models.ForeignKey(PageLayout, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    edited = models.BooleanField(default=False)
    last_modification = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
    body = RichTextUploadingField()
    deleted = models.BooleanField(default=False, blank=False)
    def __str__(self):
        return self.title

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    edited = models.BooleanField(default=False)
    last_modification = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
    body = models.CharField(max_length=1000, help_text="Maximum 1000 characters")
    deleted = models.BooleanField(default=False, blank=False)


class CustomHTML(models.Model):
    parent = models.ForeignKey(PageLayout, on_delete=models.CASCADE)
    body = RichTextUploadingField()