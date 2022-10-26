from django.urls import path
from .views import  home

app_name = "document"

urlpatterns = [
    path('', home, name="home"),
]
