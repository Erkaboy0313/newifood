from django import template
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType


register = template.Library()

@register.simple_tag
def count_comments(object):
    content_type = ContentType.objects.get_for_model(object)
    return Comment.objects.filter(content_type = content_type,object_id = object.id).count()

