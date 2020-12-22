from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	# path('current-user2/', views.currentUser2, name="current_user2"),
	path('notices-list/', views.notices_list, name="notices_list"),

	path('todo-list/', views.todo_list.as_view(), name='todolistcreate'),
	

	
	# path('test-list/', views.test_list, name='testlistcreate'),
]


