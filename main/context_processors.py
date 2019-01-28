from main.models import Section,HomePage

def sections_processor(request):
    if request.method == 'POST':
        if request.POST.get('edit_mode'):
            request.session['edit_mode'] = True
        elif request.POST.get('normal_mode'):
            request.session['edit_mode'] = False
    sections = Section.objects.filter(parent__isnull=True).order_by('order_number', 'id') #order by
    subsections = Section.objects.filter(parent__isnull=False).order_by('order_number', 'id') #order by
    home = HomePage.objects.first()
    return {'sections': sections,'subsections':subsections,'home':home}