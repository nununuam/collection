from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('button1/', views.Button1.as_view(), name="button1"),
    
]
