from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('post/', include('post.urls')),
    path('login/', include('login.urls'))
]
