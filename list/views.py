from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to the list!'))
            todo = List.objects.all()
            return render(request, 'list/home.html', {'todo':todo})
    else:
        todo = List.objects.all()
        return render(request, 'list/home.html', {'todo':todo})

def about(request):
    return render(request, 'list/about.html')

def delete(request, list_id):
    todo = List.objects.get(pk=list_id)
    todo.delete()
    messages.success(request, ('Item has been deleted from the list!'))
    return redirect('home')

def cross_off(request, list_id):
    todo = List.objects.get(pk=list_id)
    todo.completed = True
    todo.save()
    return redirect('home')

def uncross(request, list_id):
    todo = List.objects.get(pk=list_id)
    todo.completed = False
    todo.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        todo = List.objects.get(pk=list_id)

        form = ListForm(request.POST or None, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Edited!'))
            return redirect('home')
    else:
        todo = List.objects.get(pk=list_id)
        return render(request, 'list/edit.html', {'todo':todo})