from main.models import Section,Subsection

def sections_processor(request):
    sections = Section.objects.all() #order by
    subsections = Subsection.objects.all() #order by
    return {'sections': sections,'subsections':subsections}