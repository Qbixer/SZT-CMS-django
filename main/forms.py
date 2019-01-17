from django.forms import ModelForm
from django import forms

from main.models import Section,PageLayout,Post,PostComment

class SectionForm(ModelForm):   
    class Meta:
        model = Section
        exclude = ['deleted','parent']
        widgets = {
            'background_color': forms.TextInput(attrs={'class':"form-control",'type':"color"})
        }

class PageLayoutForm(ModelForm):
    class Meta:
        model = PageLayout
        fields = ('content_type','title','order_number')
        widgets = {
            'content_type': forms.Select(attrs={'class':"form-control"}),
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'order_number': forms.NumberInput(attrs={'class':"form-control"})
        }

class PageLayoutEditForm(ModelForm):
    class Meta:
        model = PageLayout
        fields = ('title','order_number')
        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
            'order_number': forms.NumberInput(attrs={'class':"form-control"})
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')
        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control"}),
        }

class PostCommentForm(ModelForm):
    class Meta:
        model = PostComment
        exclude = ['post','user','edited','last_modification']