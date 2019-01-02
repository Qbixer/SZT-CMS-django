from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    url(r'edit/section/(?P<section_id>[0-9]{1,})$',views.category_view, name="edit-section"),
    url(r'edit/subsection/(?P<subsection_id>[0-9]{1,})$',views.category_view, name="edit-subsection"),
    url(r'add/section/$',views.add_section, name="add-section"),
    url(r'add/subsection/$',views.category_view, name="add-subsection"),
    #url(r'(?P<slug>[a-z1-3_]{1,})/$',views.category_view, name="category-view"),


]