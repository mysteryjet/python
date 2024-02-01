from django.shortcuts import render, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, owner=request.user)
    return render(request, 'task_detail.html', {'task': task})
