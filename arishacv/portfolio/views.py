from django.shortcuts import render, redirect
from .models import Education, Skill, Experience, Project, Contact, Owner
from .forms import ContactForm

def index(request):
    education_list = Education.objects.all()
    skills_list = Skill.objects.all()
    experience_list = Experience.objects.all()
    projects_list = Project.objects.all()
    owner_info = Owner.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'portfolio/index.html', {
        'education': education_list,
        'skills': skills_list,
        'experience': experience_list,
        'projects': projects_list,
        'form': form,
        'owner': owner_info
    })
