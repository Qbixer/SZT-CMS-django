from django import template

register = template.Library()

@register.filter
def filter_sections(subsections, parent):
    return subsections.filter(parent=parent).filter(hidden=False).filter(deleted=False)


@register.filter
def addstr(arg1, arg2):
    return str(arg1) + str(arg2)

@register.filter
def update_variable(value):
    data = value
    return data