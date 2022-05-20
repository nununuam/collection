from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('authorStatement/', views.AuthorStatement.as_view(), name="authorStatement"),
    path('button1/', views.Button1.as_view(), name="button1"),
    path('button2/', views.Button1.as_view(), name="button1"),
    path('button3/', views.Button1.as_view(), name="button1"),
    path('button4/', views.Button1.as_view(), name="button1"),
    path('button5/', views.Button1.as_view(), name="button1"),
    path('button6/', views.Button1.as_view(), name="button1"),
    path('button7/', views.Button1.as_view(), name="button1"),
    path('button8/', views.Button1.as_view(), name="button1"),
    path('button9/', views.Button1.as_view(), name="button1"),
    path('button10/', views.Button1.as_view(), name="button1"),
    path('button11/', views.Button1.as_view(), name="button1"),
    path('button12/', views.Button1.as_view(), name="button1"),
    path('button13/', views.Button1.as_view(), name="button1"),
    path('button14/', views.Button1.as_view(), name="button1"),
    path('button15/', views.Button1.as_view(), name="button1"),
    path('button16/', views.Button1.as_view(), name="button1"),
]
