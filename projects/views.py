from django.shortcuts import render
from .models import Projects

def projects_view(request):
    projects = Projects.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})