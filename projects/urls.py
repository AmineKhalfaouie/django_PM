from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project_list'),
    path('project/create/', views.ProjectCreateView.as_view(),name='project_create')
]