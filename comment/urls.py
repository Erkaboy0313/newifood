from django.urls import path
from .views import create_comment,contact_us

urlpatterns = [
    path('create_comment/',create_comment,name='create_comment'),
    path('contact/',contact_us,name='contactus')
]
