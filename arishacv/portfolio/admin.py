# portfolio/admin.py
from django.contrib import admin
from .models import Education, Skill, Experience, Project, Contact

admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contact)
