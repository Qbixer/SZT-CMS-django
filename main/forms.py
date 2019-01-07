from django.forms import ModelForm
from main.models import Section

class SectionForm(ModelForm):   
    class Meta:
        model = Section
        exclude = ['deleted','parent']