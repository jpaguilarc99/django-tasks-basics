from django.contrib import admin
from .models import Project, Task


def register_models(*models):
    for model in models:
        admin.site.register(model)

register_models(Project, 
                Task)