from django.contrib import admin
from .models import Fruit,Section

@admin.register(Fruit)
class PostAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'like', 'seen', 'confirmed']
    list_filter = ['country', 'created_time', 'like', 'seen']
    search_fields = ['name', 'description']
    date_hierarchy = 'created_time'
    ordering = ['like', 'seen']

admin.site.register(Section)