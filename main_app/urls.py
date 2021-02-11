from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('phones/', views.phone_index, name='phone_index'),
    path('phones/<int:phone_id>/', views.phone_detail, name='phone_detail'),
]