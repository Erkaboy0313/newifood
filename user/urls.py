from django.urls import path
from .views import log_in,log_out,register,profile,create_meal,create_fruit,create_vegetable,edit_fruit,edit_meal,edit_vegetable,delete_meal,delete_fruit,delete_vegetable,\
change_meal_status,change_vegetable_status,change_fruit_status
app_name = 'user'

urlpatterns = [
    path('register/',register,name='register'),
    path('logout/',log_out,name='logout'),
    path('login/',log_in,name='login'),
    path('profile/',profile,name='profile'),
    path('profile/<str:cat>/',profile,name='profile_cat'),
    path('create-blog/meal/',create_meal,name='create_meal'),
    path('create-blog/fruit/',create_fruit,name='create_fruit'),
    path('create-blog/vegetable/',create_vegetable,name='create_vegetable'),
    path('edit-blog/fruit/<slug:slug>/',edit_fruit,name='edit_fruit'),
    path('edit-blog/meal/<slug:slug>/',edit_meal,name='edit_meal'),
    path('edit-blog/vegetable/<slug:slug>/',edit_vegetable,name='edit_vegetable'),
    path('delete-meal/<slug:slug>/',delete_meal,name='delete_meal'),
    path('delete-fruit/<slug:slug>/',delete_fruit,name='delete_fruit'),
    path('delete-vegetable/<slug:slug>/',delete_vegetable,name='delete_vegetable'),
    path('update-meal/<slug:slug>/',change_meal_status,name='change_meal_status'),
    path('update-vegetable/<slug:slug>/',change_vegetable_status,name='change_vegetable_status'),
    path('update-fruit/<slug:slug>/',change_fruit_status,name='change_fruit_status'),
]
