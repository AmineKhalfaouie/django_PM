from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(),name='project_list'),
    path('project/create/', views.ProjectCreateView.as_view(),name='project_create'),
    path('project/<int:pk>/update/', views.ProjectUpdateView.as_view(),name='project_update'),
    path('project/<int:pk>/delete', views.ProjectDeleteView.as_view(),name='project_delete'),
    path('task/create/', views.TaskCreateView.as_view(),name='task_create'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(),name='task_delete'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(),name='task_update')
]