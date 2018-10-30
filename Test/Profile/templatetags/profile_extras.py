from django import template
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('profile/edit_list.html')
def edit_list(*args):
    urls = []
    for obj in args:
        link = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        urls.append((link,  str(obj)))
    return {'urls': urls}
