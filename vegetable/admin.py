from django.contrib import admin
from .models import Vegetable,Section

@admin.register(Vegetable)
class PostAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'like', 'seen', 'key_words']
    list_filter = ['country', 'created_time', 'like', 'seen']
    search_fields = ['name', 'description']
    date_hierarchy = 'created_time'
    ordering = ['like', 'seen']

admin.site.register(Section)