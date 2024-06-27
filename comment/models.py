from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils import timezone
from django.db import models

class Comment(models.Model):
    username = models.CharField(max_length = 100,blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    reply = models.ForeignKey('self',on_delete = models.CASCADE,blank=True, null=True)
    like = models.PositiveIntegerField(default = 0)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Generic foreign key to associate with any model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    

class SiteVisit(models.Model):
    date = models.DateField(default=timezone.now)
    total_visits = models.PositiveIntegerField(default=0)
    unique_visits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.date)


class ContactUs(models.Model):
    name = models.CharField(max_length = 50,blank=True, null=True)
    email = models.EmailField(max_length = 50,blank=True, null=True)
    text = models.TextField(blank=True, null=True)