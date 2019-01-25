from django.shortcuts import render, redirect
from django.core.mail.backends.smtp import EmailBackend
from .models import MailConfiguration
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    mailConfig = MailConfiguration.objects.first()
    with get_connection(
      host=mailConfig.host, 
      username=mailConfig.address, 
      password="asd", 
      use_tls=True
    ) as connection:
      EmailMessage('diditwork?', 'test message', '', ['qbixer@gmail.com','jakub.falkowski33@gmail.com'],
                  connection=connection).send()
    return redirect('main_index')
