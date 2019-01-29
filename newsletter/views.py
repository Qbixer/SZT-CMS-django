from django.shortcuts import render, redirect
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.message import EmailMessage
from .models import EmailSent,NewsletterUser
from .forms import EmailSentForm

from django.core.mail import get_connection, send_mail,EmailMultiAlternatives
from django.template import Context, Template
from main.models import MailConfiguration,EmailTemplate
from django.urls import reverse
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def index(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.POST.get('send_emails'):
      form = EmailSentForm(request.POST)
      if form.is_valid():
        mailConfig = MailConfiguration.objects.first()
        if mailConfig is None:
          return render(request, 'main/error.html')
        newsletterEmailTemplate = EmailTemplate.objects.get(email_type='deactivate_newsletter')
        if newsletterEmailTemplate is None:
          return render(request, 'main/error.html')
        users = NewsletterUser.objects.filter(activated=True).values('email','delete_code')
        email_list = list(map(lambda x: x['email'], users))
        if len(users) > 0:
          email = form.save(commit=False)
          try:
            with get_connection(
              host=mailConfig.host, 
              username=mailConfig.address, 
              password=mailConfig.password, 
              use_tls=True
            ) as connection:
              current_site = get_current_site(request)
              for user in users:
                context = Context({
                    'delete_link':"http://"+current_site.domain+reverse('deactivate_newsletter',args=[user['delete_code']])
                    })
                message = Template(newsletterEmailTemplate.body).render(context)
                wholeEmail = email.body+message
                msg = EmailMultiAlternatives(email.title, strip_tags(wholeEmail), mailConfig.address, [user['email']], connection=connection)
                msg.attach_alternative(wholeEmail, "text/html")
                msg.send()
            email.save()
          except Exception as e:
            print(e)
            return render(request, 'main/error.html')   
        else:
          email.save()    
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

def delete_account(request, delete):
  newsletterUser = NewsletterUser.objects.get(delete_code=delete)
  if newsletterUser is not None:
    newsletterUser.delete()
    return render(request,'newsletter/delete_newsletter.html')   
  else:
    return render(request, 'main/error.html')