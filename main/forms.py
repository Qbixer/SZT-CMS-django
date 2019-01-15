from django.forms import ModelForm
from main.models import Section,PageLayout

class SectionForm(ModelForm):   
    class Meta:
        model = Section
        exclude = ['deleted','parent']

class PageLayoutForm(ModelForm):
    class Meta:
        model = PageLayout
        exclude = ['section']