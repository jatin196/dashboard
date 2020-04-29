from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from .models import Task
from .forms import TodoForm

# class TodoList(generic.ListView):
#     model = Task
#     context_object_name = 'TL'
#     template_name =

def TodoList(requset):
    tasks = Task.objects.all()
    context = {
        'TL': tasks
    }
    return render(requset, 'todo/index.html', context)

def Update(request, id):
    task = get_object_or_404(Task, id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.instance.user = request.user
        form.save()

    context = {
        'form' : form
    }
    return render(request, 'todo/TodoForm.html', context)

def create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect(reverse('todo-list'))
    context = {
        'form': form
    }
    return render(request, 'todo/TodoForm.html', context)

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect(reverse('todo-list'))


