from django.urls import path
from .views import fruitdetails,search_result,fruits,contact_us,like_post
app_name = 'fruit'

urlpatterns = [
    path('',fruits,name='fruits'),
    path('fruit-details/<str:region>/<str:country>/<int:year>/<int:month>/<int:day>/<slug:post>/',fruitdetails,name='fruit_details'),
    path('search-result/',search_result,name='search'),
    path('contact/',contact_us,name='contact'),
    path('like-post/<int:post_id>/', like_post, name='like_post'),
]
