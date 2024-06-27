from django.urls import path
from .views import vegetable_details,vegetables,like_post
app_name = 'vegetable'

urlpatterns = [
    path("",vegetables,name="vegetables"),
    path('<str:type>/',vegetables,name='vegetable_by_region'),
    path('like-post/<int:post_id>/', like_post, name='like_post'),
    path('<str:region>/<str:country>/<int:year>/<int:month>/<int:day>/<slug:post>/',vegetable_details,name='vegetable_details'),
]
