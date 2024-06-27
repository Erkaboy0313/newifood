from django.contrib import admin
from .models import Comment,SiteVisit,ContactUs


admin.site.register(Comment)
admin.site.register(ContactUs)
# Register your models here.

@admin.register(SiteVisit)
class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ['total_visits', 'unique_visits', 'date']