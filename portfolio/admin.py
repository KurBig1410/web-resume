from django.contrib import admin
from .models import About, SkillCategory, Skill, Experience, Project, Contact

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [SkillInline]

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date')
    ordering = ('-start_date',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'live_link')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'telegram', 'github', 'linkedin')

# Для отображения Skills отдельно, если захочешь
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')