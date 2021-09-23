from django.forms.forms import Form
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.


def home(request):
    if request.method == 'POST':
        todos = request.POST['todo']
        print(todos)
        data = todo(todo=todos)
        data.save()
        return redirect('/home/')
    else:
        todos = todo.objects.all()
        return render(request, 'home.html', {"todos": todos})


def delete(request, id):
    todos = todo.objects.get(id=id)
    todos.delete()
    return redirect('/home/')


def update(request, id):
    todos = todo.objects.get(id=id)
    form = updateForm(instance=todos)
    if request.method == 'POST':
        form = updateForm(request.POST, instance=todos)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    return render(request, 'update.html', {'form': form})
