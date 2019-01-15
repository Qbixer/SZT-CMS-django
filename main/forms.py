from django.forms import ModelForm
from main.models import Section,PageLayout,Post

class SectionForm(ModelForm):   
    class Meta:
        model = Section
        exclude = ['deleted','parent']

class PageLayoutForm(ModelForm):
    class Meta:
        model = PageLayout
        exclude = ['section']

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['parent']