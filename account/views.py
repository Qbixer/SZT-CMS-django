from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from account.forms import SignUpForm
from account.tokens import account_activation_token

from django.core.mail import get_connection, send_mail,EmailMultiAlternatives
from django.template import Context, Template
from main.models import MailConfiguration,EmailTemplate
from django.urls import reverse
from django.utils.html import strip_tags


def signup(request):
    if not request.user.is_anonymous:
        return redirect('main_index')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            mailConfig = MailConfiguration.objects.first()
            if mailConfig is None:
                return render(request, 'main/error.html')
            newsletterEmailTemplate = EmailTemplate.objects.get(email_type='activate_account')
            if newsletterEmailTemplate is None:
                return render(request, 'main/error.html')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            try:
                with get_connection(
                    host=mailConfig.host, 
                    username=mailConfig.address, 
                    password=mailConfig.password, 
                    use_tls=True
                ) as connection:
                    current_site = get_current_site(request)
                    uid = force_text(urlsafe_base64_encode(force_bytes(user.id)))
                    token = account_activation_token.make_token(user)
                    context = Context({
                        'activate_link':"http://"+current_site.domain+reverse('activate',args=[uid,token]),
                        'username':user.username
                        })
                    message = Template(newsletterEmailTemplate.body).render(context)
                    msg = EmailMultiAlternatives(newsletterEmailTemplate.subject, strip_tags(message), mailConfig.address, [user.email], connection=connection)
                    msg.attach_alternative(message, "text/html")
                    msg.send()
            except Exception as e:
                return render(request, 'main/error.html')
        return redirect('main_index')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64).decode())
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect('main_index')
    else:
        return render(request, 'account/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'account/account_activation_sent.html')