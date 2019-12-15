from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.home),    #Preliminary Home Page
    path('admin/', admin.site.urls),
]
