from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import About, SkillCategory, Experience, Project, Contact
from .serializers import (
    AboutSerializer, SkillCategorySerializer, ExperienceSerializer,
    ProjectSerializer, ContactSerializer
)

@api_view(['GET'])
def about_view(request):
    about = About.objects.first()
    serializer = AboutSerializer(about)
    return Response(serializer.data)

@api_view(['GET'])
def skills_view(request):
    skills = SkillCategory.objects.prefetch_related('skills').all()
    serializer = SkillCategorySerializer(skills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def experience_view(request):
    experience = Experience.objects.order_by('-start_date')
    serializer = ExperienceSerializer(experience, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def projects_view(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def contacts_view(request):
    contact = Contact.objects.first()
    serializer = ContactSerializer(contact)
    return Response(serializer.data)