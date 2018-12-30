from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'(?P<slug>[a-z1-3_]{1,})/$',views.category_view, name="category-view"),
    path('', views.index, name='main.index'),

]