from django.urls import path
from . import views

urlpatterns = [
    path('', views.ParcelList.as_view(), name='listcreate'),
	path('<int:pk>/', views.ParcelDetail.as_view(), name='detailcreate'),
    path('create/', views.CreateParcel.as_view(), name='createpost'),
    path('edit/<int:pk>/', views.EditParcel.as_view(), name='editpost'),
    path('delete/<int:pk>/', views.DeleteParcel.as_view(), name='deletepost'),
]