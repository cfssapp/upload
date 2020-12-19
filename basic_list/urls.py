from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('current-user/', views.currentUser, name="current_user"),
	path('notices-list/', views.notices_list, name="notices_list"),

	path('basic-list/', views.basic_list.as_view(), name='listcreate'),
	path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

	path('test-list/', views.test_list, name='testlistcreate'),
]


