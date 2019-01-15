from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from main.models import Section,PageLayout
from main.forms import SectionForm,PageLayoutForm
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def section_view(request, section_url):
    section = Section.objects.filter(url=section_url).order_by('id').first()
    pageLayouts = PageLayout.objects.filter(section=section).order_by('order_number','id')
    
    pageLayoutForm = PageLayoutForm
    return render(request, 'main/custom_page.html', {
        'title':section.title,
        'pageLayoutForm':pageLayoutForm
    })

def subsection_view(request, section_url, subsection_url):
    html = Section.objects.filter(parent__url=section_url, url=subsection_url).first()
    return render(request, 'main/custom_page.html', {
        'title':html.title,
    })

def add_section(request):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.method == 'POST':
        if request.POST.get('add_section'):
            form = SectionForm(request.POST)
            if form.is_valid():
                section = form.save(commit=False)
                section.parent = None
                section.save()
                return redirect('main_index')
        else:
            form = SectionForm()
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
        if request.POST.get('edit_section'):
            form = SectionForm(request.POST,instance=section)
            if form.is_valid():
                form.save()
                return redirect('main_index')
        else:
            form = SectionForm(instance=section)
    else:
        form = SectionForm(instance=section)
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Edit section",
        'edit':True
    })

def add_subsection(request,section_id):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    if request.method == 'POST':
        if request.POST.get('add_section'):
            form = SectionForm(request.POST)
            if form.is_valid():
                subsection = form.save(commit=False)
                section = Section.objects.get(id=section_id)
                subsection.parent = section
                subsection.save()
                return redirect('main_index')
        else:
            form = SectionForm()
    else:
        form = SectionForm()
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Add subsection",
        'edit':False

    })

def edit_subsection(request,subsection_id):
    current_user = request.user
    if current_user.is_anonymous or not (current_user.is_superuser or current_user.is_staff or current_user.profile.moderator):
        return redirect('main_index')
    subsection = Section.objects.get(id=subsection_id)
    if request.method == 'POST':
        if request.POST.get('edit_section'):
            form = SectionForm(request.POST,instance=subsection)
            if form.is_valid():
                form.save()
                return redirect('main_index')
        else:
            form = SectionForm(instance=subsection)
    else:
        form = SectionForm(instance=subsection)
    return render(request, 'main/edit_section.html', {
        'form':form,
        'title':"Edit subsection",
        'edit':True
    })
