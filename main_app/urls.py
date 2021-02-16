from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('phones/', views.phones_index, name='phones_index'),
    path('phones/<int:phone_id>/', views.phone_detail, name='phone_detail'),
    path('phones/create/', views.PhoneCreate.as_view(), name='phones_create'),
    path('phones/<int:pk>/update', views.PhoneUpdate.as_view(), name='phones_update'),
    path('phones/<int:pk>/delete', views.PhoneDelete.as_view(), name='phones_delete'),
    path('cases/', views.cases_index, name='cases_index'),
    path('cases/<int:case_id>/', views.case_detail, name='case_detail'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>/update', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete', views.CaseDelete.as_view(), name='cases_delete'),
]
