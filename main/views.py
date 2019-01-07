from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from main.models import Section
from main.forms import SectionForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def category_view(request, section_url):
    html = Section.objects.get(url=section_url)
    return render(request, 'main/custom_page.html', {
        'title':"Edit section",
    })

def add_section(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.parent = None
            section.save()
            return redirect('main_index')
    else:
        form = SectionForm()
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Add section",
        'edit':False

    })

def edit_section(request,section_id):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    section = Section.objects.get(id=section_id)
    if request.method == 'POST':
        form = SectionForm(request.POST,instance=section)
        if form.is_valid():
            form.save()
            return redirect('main_index')
    form = SectionForm(instance=section)
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Edit section",
        'edit':True
    })
