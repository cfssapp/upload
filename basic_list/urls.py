from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('notices-list/', views.notices_list, name="notices_list"),
	path('todo-list/', views.todo_list.as_view(), name='todolistcreate'),

	path('post/<int:pk>/', views.PostDetail.as_view(), name='detailcreate'),
    path('post/', views.PostList.as_view(), name='listcreate'),
	
    path('post/create/', views.CreatePost.as_view(), name='createpost'),
    path('post/edit/postdetail/<int:pk>/', views.AdminPostDetail.as_view(), name='admindetailpost'),
    path('post/edit/<int:pk>/', views.EditPost.as_view(), name='editpost'),
    path('post/delete/<int:pk>/', views.DeletePost.as_view(), name='deletepost'),
]


