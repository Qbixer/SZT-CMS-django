from django import template

register = template.Library()

@register.filter
def filter_sections(subsections, parent):
    return subsections.filter(parent=parent).filter(hidden=False).filter(deleted=False)

