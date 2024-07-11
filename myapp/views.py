from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject

import pandas as pd


def index(request):
    title = 'Plataforma de Innovacion'
    return render(request, 'index.html', {'title': title})


def about(request):
    username = 'JPAGUILARC'
    return render(request, 'about.html', {'username': username})


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


def tables(request):
    df = pd.DataFrame({
        'Nombre': ['Tarea 1', 'Tarea 2'],
        'Estado': ['Completado', 'Pendiente']
    })
    df_html = df.to_html()
    context = {'df_html': df_html}
    return render(request, 'tables.html', context)


def create_task(request):
    if request.method == "GET":
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],
                            project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            "form": CreateNewProject(),
        })
    else:        
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
