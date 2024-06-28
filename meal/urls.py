from django.urls import path
from .views import meal_details,meals,like_post,create_countries,create_meal
app_name = 'meal'
from django.contrib.sitemaps.views import sitemap
from .sitemaps import MealSitemap
sitemaps = {
    'meals': MealSitemap,
}
urlpatterns = [
    path('',meals,name='meals'),
    # path('crete-countries/',create_countries),
    # path('crete-meal/',create_meal),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('<slug:region>/',meals,name='meal_by_region'),
    path('like-post/<int:post_id>/', like_post, name='like_post'),
    path('<str:region>/<str:country>/<int:year>/<int:month>/<int:day>/<slug:post>/',meal_details,name='meal_details'),
]
