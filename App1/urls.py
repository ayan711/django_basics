from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('user/', views.user),
    path('login/', views.login),
    path('about/',views.about)
]