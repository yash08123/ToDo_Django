from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Todo
from django.contrib import messages

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/todo_list.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Todo.objects.create(
                title=title,
                description=description,
                user=request.user
            )
            messages.success(request, 'Todo added successfully!')
        return redirect('todo_list')
    return render(request, 'todo/add_todo.html')

@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')

@login_required
def complete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = True
    todo.save()
    messages.success(request, 'Todo marked as complete!')
    return redirect('todo_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'todo_list')
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
