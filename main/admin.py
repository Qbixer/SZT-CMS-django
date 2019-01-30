from django.contrib import admin
from .models import *
admin.site.register(Post)
admin.site.register(MailConfiguration)
admin.site.register(ContentType)
admin.site.register(Section)
admin.site.register(HomePage)
admin.site.register(PageLayout)
admin.site.register(PostComment)
admin.site.register(CustomHTML)


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
  fields = ('email_type','subject','body','helper_text')
  readonly_fields = ('email_type','helper_text')

