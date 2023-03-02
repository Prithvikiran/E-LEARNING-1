from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from base.models import User

from .models import Todo
from .forms import TodoForm

def index(request):
    try:
      todo_list = Todo.objects.filter(user=request.user)
    except Todo.DoesNotExist:
        todo_list = []


    form = TodoForm()

    context = {'todo_list' : todo_list, 'form' : form,'user':request.user}

    return render(request, 'focuzz/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'],user=request.user)
        new_todo.save()

    return redirect('to_do')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('to_do')

def deleteCompleted(request):
    Todo.objects.filter(user=request.user).filter(complete__exact=True).delete()

    return redirect('to_do')

def deleteAll(request):

    Todo.objects.filter(user=request.user).all().delete()

    return redirect('to_do')

def startTask(request):
    return render(request,'focuzz/timer.html',{})