from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('authorStatement/', views.AuthorStatement.as_view(), name="authorStatement"),
    path('button1/', views.Button1.as_view(), name="button1"),
    path('button2/', views.Button2.as_view(), name="button2"),
    path('button3/', views.Button3.as_view(), name="button3"),
    path('button4/', views.Button4.as_view(), name="button4"),
    path('button5/', views.Button5.as_view(), name="button5"),
    path('button6/', views.Button6.as_view(), name="button6"),
    path('button7/', views.Button7.as_view(), name="button7"),
    path('button8/', views.Button8.as_view(), name="button8"),
    path('button9/', views.Button9.as_view(), name="button9"),
    path('button10/', views.Button10.as_view(), name="button10"),
    path('button11/', views.Button11.as_view(), name="button11"),
    path('button12/', views.Button12.as_view(), name="button12"),
    path('button13/', views.Button13.as_view(), name="button13"),
    path('button14/', views.Button14.as_view(), name="button14"),
    path('button15/', views.Button15.as_view(), name="button15"),
    path('button16/', views.Button16.as_view(), name="button16"),
]
