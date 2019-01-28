from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='newsletter_index'),
    path('configure_email', views.index, name='configure_email'),
    url(r'^activate/(?P<activate>[0-9A-Za-z]{64})',
        views.activate_account, name='activate_newsletter'),
]