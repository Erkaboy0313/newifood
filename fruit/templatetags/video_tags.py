from django import template
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.utils.html import strip_tags
from django.template.defaultfilters import truncatewords


register = template.Library()

@register.simple_tag
def count_comments(object):
    content_type = ContentType.objects.get_for_model(object)
    return Comment.objects.filter(content_type = content_type,object_id = object.id).count()

@register.filter(name='strip_html_and_truncate')
def strip_html_and_truncate(value, arg):
    stripped = strip_tags(value)
    truncated = truncatewords(stripped, arg)
    return truncated