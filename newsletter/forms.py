from django.forms import ModelForm
from django import forms
from .models import NewsletterUser,MailConfiguration,EmailSent

class NewsletterUserForm(ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={'class':"form-control"}),
        }

class MailConfigurationForm(ModelForm):
    class Meta:
        model = MailConfiguration
        fields = ('host','address','password')
        widgets = {
            'host': forms.TextInput(attrs={'class':"form-control",'maxlength':"255"}),
            'address': forms.EmailInput(attrs={'class':"form-control"}),
            'password': forms.PasswordInput(attrs={'class': "form-control"})
        }

class EmailSentForm(ModelForm):
    class Meta:
        model = EmailSent
        fields = ('title','body')
        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control",'maxlength':"200","required":'true'}),
        }
