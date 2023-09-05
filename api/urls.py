from subapp.views import index,people,main
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    
    path('index/', index),
    path('people/',people),
    
    path('main/',main.as_view())
    
]