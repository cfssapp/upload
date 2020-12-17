from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview.as_view(), name="api-overview"),
	path('basic-list/', views.basic_list.as_view(), name='listcreate'),
	path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]


