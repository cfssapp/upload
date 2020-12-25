from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	
	path('notices-list/', views.notices_list, name="notices_list"),

	path('todo-list/', views.todo_list.as_view(), name='todolistcreate'),

	path('post/<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('post', PostList.as_view(), name='listcreate'),
	
]


