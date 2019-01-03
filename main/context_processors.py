from main.models import Section,Subsection

def sections_processor(request):
    sections = Section.objects.all().order_by('order_number', 'id') #order by
    subsections = Subsection.objects.all().order_by('order_number', 'id') #order by
    return {'sections': sections,'subsections':subsections}