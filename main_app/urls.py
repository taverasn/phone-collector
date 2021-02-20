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
    path('phones/<int:phone_id>/add_usage', views.add_usage, name='add_usage'),
    path('phones/<int:phone_id>/add_photo/', views.add_photo, name='add_photo'),
    path('phones/<int:phone_id>/assoc_case/<int:case_id>/', views.assoc_case, name='assoc_case'),
    path('phones/<int:phone_id>/unassoc_case/<int:case_id>/', views.unassoc_case, name='unassoc_case'),
    path('cases/', views.CaseList.as_view(), name='cases_index'),
    path('cases/<int:pk>/', views.CaseDetail.as_view(), name='case_detail'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>/update', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete', views.CaseDelete.as_view(), name='cases_delete'),
    path('accounts/signup', views.signup, name='signup')
]
