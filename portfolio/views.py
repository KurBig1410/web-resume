from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import About, SkillCategory, Experience, Project, Contact
from .serializers import (
    AboutSerializer, SkillCategorySerializer, ExperienceSerializer,
    ProjectSerializer, ContactSerializer
)
from django.shortcuts import render
from django.shortcuts import get_object_or_404


import markdown
from django.utils.safestring import mark_safe

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    rendered_description = mark_safe(markdown.markdown(project.description))
    return render(request, 'myresume/project_detail.html', {
        'project': project,
        'description_html': rendered_description
    })



def resume_view(request):
    about = About.objects.first()
    skills = SkillCategory.objects.prefetch_related('skills').all()
    projects = Project.objects.all()
    contact = Contact.objects.first()

    return render(request, 'myresume/resume.html', {
        'about': about,
        'skills': skills,
        'projects': projects,
        'contact': contact
    })

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