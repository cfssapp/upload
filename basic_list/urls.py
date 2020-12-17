from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('currentUser/', views.currentUser, name="currentUser"),

	path('basic-list/', views.basic_list.as_view(), name='listcreate'),
	path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]


