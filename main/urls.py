from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('edit/main',views.edit_main,name='edit_main'),
    path('edit/section/<int:section_id>/',views.edit_section, name="edit_section"),
    path('edit/subsection/<int:subsection_id>',views.edit_subsection, name="edit_subsection"),
    path('add/section/',views.add_section, name="add_section"),
    path('add/<int:section_id>/subsection/',views.add_subsection, name="add_subsection"),
    path('<section_url>',views.section_view, name="section"),
    path('<section_url>/<subsection_url>',views.subsection_view, name="subsection"),
]