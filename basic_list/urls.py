from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('current-user2/', views.currentUser2, name="current_user2"),
	path('notices-list/', views.notices_list, name="notices_list"),

	path('basic-list/', views.basic_list.as_view(), name='listcreate'),
	path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

	path('current-user/', views.currentUser.as_view(), name="current_user"),
	path('current-user/<int:pk>/', views.currentUserDetail.as_view(), name="current_user_detail"),
	# path('test-list/', views.test_list, name='testlistcreate'),
]


