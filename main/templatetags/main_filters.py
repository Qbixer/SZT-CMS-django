from django import template
from django.utils.safestring import mark_safe

import json
from django.core import serializers


register = template.Library()

@register.filter
def filter_sections(subsections, parent):
    return subsections.filter(parent=parent).filter(hidden=False).filter(deleted=False)


@register.filter
def addstr(arg1, arg2):
    return str(arg1) + str(arg2)

@register.filter
def update_variable(data):
    data = False
    return data

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(list(obj)))

@register.filter(is_safe=True)
def layout_js(obj):
  data = list()
  for pageLayout in obj:
    tmp = dict()
    tmp['id'] = pageLayout.id
    if pageLayout.content_type.name == 'post':
      tmp['posts'] = []
      for post in pageLayout.posts:
        p = {}
        p['id'] = post.id
        p['edit'] = post.edit
        tmp['posts'].append(p)
    data.append(tmp)
  data.append("abc")
  return json.dumps(list(data))