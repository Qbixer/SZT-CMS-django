from django.forms import ModelForm
from main.models import Section, Subsection

class SectionForm(ModelForm):   
    class Meta:
        model = Section
        exclude = ['content']