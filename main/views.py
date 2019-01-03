from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from main.models import Section,Subsection
from main.forms import SectionForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def category_view(request, slug):
    html = Custom_HTML.objects.get(url=slug)
    t = Template(("{% extends 'main/index.html' %} {% block content %}"+html.html+"{% endblock %}"))
    text = t.render(Context({}))
    return HttpResponse(text)

def add_section(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_index')
    else:
        form = SectionForm()
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Add section"
    })

def edit_section(request,section_id):
    section = Section.objects.get(id=section_id)
    form = SectionForm(instance=section)
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Edit section",
    })
