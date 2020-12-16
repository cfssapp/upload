from django.urls import path
from . import views

urlpatterns = [
	# path('', views.apiOverview, name="api-overview"),
	path('basic-list/', views.basic_list.as_view(), name='listcreate'),
]


