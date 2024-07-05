from django.contrib import admin
from .models import Meal,Country,Region,Section,Locations

@admin.register(Meal)
class PostAdmin(admin.ModelAdmin):
    list_display = ['country','slug', 'name', 'like', 'seen', 'confirmed']
    list_filter = ['country', 'created_time', 'like', 'seen']
    search_fields = ['name', 'description']
    date_hierarchy = 'created_time'
    ordering = ['like', 'seen']

admin.site.register(Section)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Locations)