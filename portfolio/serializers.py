from rest_framework import serializers
from .models import About, SkillCategory, Skill, Experience, Project, Contact

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']

class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = SkillCategory
        fields = ['name', 'skills']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['full_name', 'position', 'bio', 'avatar']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company', 'position', 'start_date', 'end_date', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technologies', 'github_link', 'live_link', 'image']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['telegram', 'email', 'github', 'linkedin']