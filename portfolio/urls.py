from django.urls import path
from . import views
from .views import resume_view, project_detail


urlpatterns = [
    path('api/about/', views.about_view),
    path('api/skills/', views.skills_view),
    path('api/experience/', views.experience_view),
    path('api/projects/', views.projects_view),
    path('api/contact/', views.contacts_view),
    path('', resume_view, name='resume'),
    path('project/<int:pk>/', project_detail, name='project_detail'),
]