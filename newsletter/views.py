from django.shortcuts import render, redirect
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import get_connection, send_mail,EmailMultiAlternatives
from django.core.mail.message import EmailMessage
from .models import MailConfiguration,EmailSent,NewsletterUser
from .forms import EmailSentForm
from django.utils.html import strip_tags

# Create your views here.
def index(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.POST.get('send_emails'):
      mailConfig = MailConfiguration.objects.first()
      users = NewsletterUser.objects.filter(activated=True).values('email')
      email_list = list(map(lambda x: x['email'], users))
      if mailConfig is None:
        return render(request, 'main/error.html')
      form = EmailSentForm(request.POST)
      if form.is_valid():
        email = form.save(commit=False)
        try:
          with get_connection(
            host=mailConfig.host, 
            username=mailConfig.address, 
            password=mailConfig.password, 
            use_tls=True
          ) as connection:
            text = strip_tags(email.body)
            msg = EmailMultiAlternatives(email.title, strip_tags(email.body), mailConfig.address, bcc=email_list, connection=connection)
            msg.attach_alternative(email.body, "text/html")
            msg.send()
          email.save()
        except Exception:
          return render(request, 'main/error.html')
      return redirect('main_index')
    form = EmailSentForm()
    return render(request,'newsletter/email_form.html', {
      'form': form
    })

def activate_account(request, activate):
  newsletterUser = NewsletterUser.objects.get(activation_code=activate)
  if newsletterUser is not None:
    newsletterUser.activated = True
    newsletterUser.save()
    return render(request,'newsletter/activate_newsletter.html')   
  else:
    return render(request, 'main/error.html')