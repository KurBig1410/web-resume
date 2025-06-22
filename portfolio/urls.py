from django.urls import path
from . import views

urlpatterns = [
    path('api/about/', views.about_view),
    path('api/skills/', views.skills_view),
    path('api/experience/', views.experience_view),
    path('api/projects/', views.projects_view),
    path('api/contact/', views.contacts_view),
]