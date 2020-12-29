from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParcelList.as_view(), name='listparcel'),
	path('<int:pk>/', views.ParcelDetail.as_view(), name='detailparcel'),
    path('create/', views.CreateParcel.as_view(), name='createparcel'),
    path('edit/<int:pk>/', views.EditParcel.as_view(), name='editparcel'),
    path('delete/<int:pk>/', views.DeleteParcel.as_view(), name='deleteparcel'),
]