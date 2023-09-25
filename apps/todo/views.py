from django.shortcuts import render, redirect, get_object_or_404
from apps.todo.models import Settings
from apps.todo.forms import SettingsForm

def task_list(request):
    tasks = Settings.objects.all()
    return render(request, 'todo/task_list.html', locals())

def task_add(request):
    if request.method == 'POST':
        form = SettingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = SettingsForm()
    return render(request, 'todo/task_form.html', locals())

def task_edit(request, pk):
    task = Settings.objects.get(pk=pk)
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = SettingsForm(instance=task)
    return render(request, 'todo/task_form.html', locals())

def task_delete(request, pk):
    task = Settings.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', locals())
