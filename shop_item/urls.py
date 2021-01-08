from django.urls import path
from . import views

urlpatterns = [
    path('item/', views.ItemList.as_view(), name='listitem'),
	path('item/<int:pk>/', views.ItemDetail.as_view(), name='detailitem'),
    path('item/create/', views.CreateItem.as_view(), name='itemcreate'),
    path('item/edit/<int:pk>/', views.EditItem.as_view(), name='itemedit'),
    path('item/delete/<int:pk>/', views.DeleteItem.as_view(), name='itemdelete'),
]