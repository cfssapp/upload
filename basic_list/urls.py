from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	
	path('notices-list/', views.notices_list, name="notices_list"),

	path('todo-list/', views.todo_list.as_view(), name='todolistcreate'),

	# path('post/<int:pk>/', views.PostDetail.as_view(), name='detailcreate'),
    # path('post/', views.PostList.as_view(), name='listcreate'),
	
]


app_name = 'basic_list'

router = DefaultRouter()
router.register('', views.PostList, basename='post')
urlpatterns = router.urls