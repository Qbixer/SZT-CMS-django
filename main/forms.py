from django.forms import ModelForm

from main.models import Section,PageLayout,Post,PostComment

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
        exclude = ['parent','edited','last_modification']

class PostCommentForm(ModelForm):
    class Meta:
        model = PostComment
        exclude = ['post','user','edited','last_modification']