from django.contrib import admin
from .models import Post,EmailTemplate

admin.site.register(Post)

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
  fields = ('email_type','subject','body','helper_text')
  readonly_fields = ('email_type','helper_text')