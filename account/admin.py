from django.contrib import admin

from .models import Profile
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  fields = ('user','email_confirmed','moderator')
  readonly_fields = ('user',)

