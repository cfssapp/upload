from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	
	path('notices-list/', views.notices_list, name="notices_list"),

	path('todo-list/', views.todo_list.as_view(), name='todolistcreate'),
	
]


