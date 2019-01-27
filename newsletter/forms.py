from django.forms import ModelForm
from django import forms
from .models import NewsletterUser,MailConfiguration,EmailSent

class NewsletterUserForm(ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ('email',)

class MailConfigurationForm(ModelForm):
    class Meta:
        model = MailConfiguration
        fields = ('host','address')
        widgets = {
            'host': forms.TextInput(attrs={'class':"form-control",'maxlength':"255"}),
            'address': forms.EmailInput(attrs={'class':"form-control"})
        }

class EmailSentForm(ModelForm):
    password = forms.CharField(max_length=254,widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = EmailSent
        fields = ('title','body','password')
        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control",'maxlength':"200","required":'true'}),
        }
