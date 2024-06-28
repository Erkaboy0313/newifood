from django.contrib.sitemaps import Sitemap
from .models import Meal

class MealSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Meal.objects.all()

    def lastmod(self, obj):
        return obj.updated_time

    def location(self, obj):
        return obj.get_absolute_url()
    

static_urls = {
    'home': {'changefreq': 'daily', 'priority': 1.0},
    'fruits': {'changefreq': 'weekly', 'priority': 0.8},
    'vegetables': {'changefreq': 'weekly', 'priority': 0.8},
    'meals': {'changefreq': 'weekly', 'priority': 0.8},
}