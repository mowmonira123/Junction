from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Junction-home'),
    path('about/', views.about, name='Junction-about'),
]
