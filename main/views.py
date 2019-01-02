from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from main.models import Section,Subsection
from main.forms import SectionForm
# Create your views here.
def index(request):
    current_user = request.user
    l = request.user.groups.values_list('name',flat=True)
    return render(request, 'main/index.html')

def category_view(request, slug):
    html = Custom_HTML.objects.get(url=slug)
    t = Template(("{% extends 'main/index.html' %} {% block content %}"+html.html+"{% endblock %}"))
    text = t.render(Context({}))
    return HttpResponse(text)

def add_section(request):
    form = SectionForm()
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Add section"
    })