from django.shortcuts import render, redirect
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import get_connection, send_mail,EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from .models import MailConfiguration,EmailSent
from .forms import EmailSentForm
from django.utils.html import strip_tags

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.POST.get('send_emails'):
      mailConfig = MailConfiguration.objects.first()
      if mailConfig is None or request.POST.get('password') is None:
        return redirect('main_index')      
      form = EmailSentForm(request.POST)
      if form.is_valid():
        email = form.save(commit=False)
        try:
          with get_connection(
            host=mailConfig.host, 
            username=mailConfig.address, 
            password=request.POST.get('password'), 
            use_tls=True
          ) as connection:
            text = strip_tags(email.body)
            msg = EmailMultiAlternatives(email.title, strip_tags(email.body), mailConfig.address, ['qbixer@gmail.com'], connection=connection)
            msg.attach_alternative(email.body, "text/html")
            msg.send()
          email.save()
        except Exception:
          return render(request, 'main/404.html')
      return redirect('main_index')
    form = EmailSentForm()
    return render(request,'newsletter/email_form.html', {
      'form': form
    })
