from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from main.models import *
# Create your views here.
def index(request):
    sections = Section.objects.all()
    subsections = Subsection.objects.all()
    subsubsections = Subsubsection.objects.all()
    return render(request, 'main/index.html', {
        'sections':sections,
        'subsections':subsections,
        'subsubsections':subsubsections
    })

def category_view(request, slug):
    html = Custom_HTML.objects.get(url=slug)
    t = Template(("{% extends 'main/index.html' %} {% block content %}"+html.html+"{% endblock %}"))
    text = t.render(Context({}))
    return HttpResponse(text)