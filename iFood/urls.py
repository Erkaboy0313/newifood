"""
URL configuration for iFood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from fruit.views import home
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',RedirectView.as_view(url = 'home/')), # redirects ('') to ('home/')
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('fruits/',include('fruit.urls')),
    path('vegetables/',include('vegetable.urls')),
    path('meals/',include('meal.urls')),
    path('comment/',include('comment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
