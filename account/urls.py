from django.conf.urls import url
from account import views as account_views

urlpatterns = [
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^account_activation_sent/$', account_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        account_views.activate, name='activate'),
]