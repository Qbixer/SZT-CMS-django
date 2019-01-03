from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('edit/section/<int:section_id>/',views.edit_section, name="edit_section"),
    url(r'edit/subsection/(?P<subsection_id>[0-9]{1,})$',views.category_view, name="edit_subsection"),
    path('add/section/',views.add_section, name="add_section"),
    url(r'add/subsection/$',views.category_view, name="add_subsection"),
    #url(r'(?P<slug>[a-z1-3_]{1,})/$',views.category_view, name="category-view"),


]