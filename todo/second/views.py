from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from .models import Favourite, Todo
from .forms import FavouriteForm, FavouriteModelForm, TodoForm, TodoModelForm


# Create your views here.
def index(request):
    return render(request, "second/index.html")

def favourite(request):
    data = Favourite.objects.all()
    return render(request, "second/favourite.html",
        {'datas':data}
    )

def favourite_detail(request, seq):
    detail = Favourite.objects.get(pk=seq)
    # detail = Favourite.objects.get(seq=seq)
    return render(request, "second/favourite_detail.html",{
        'detail': detail
    })

def favourite_register(request):
    if request.method == 'GET':
        # form = StudentForm()
        form = FavouriteModelForm()
        return render(request, 'second/favourite_register.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = FavouriteModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("second:favourite")
        else:
             return render(request, 'second/favourite_register.html', {
                'form':form
            })

def todo(request):
    
    pendings = Todo.objects.filter(status='pending')
    inprogress = Todo.objects.filter(status='inprogress')
    ends = Todo.objects.filter(status='end')
    
    # data = Todo.objects
    
    # if 'group' in request.GET:
    #     data = data.filter(group__name=request.GET['group'])
    
    # if 'end_date' in request.GET:
    #     data = data.filter(end_date__gte=request.GET['end_date'])
    
    return render(request, "second/todo.html",
        {
            'pendings':pendings,
            'inprogress':inprogress,
            'ends':ends
        }
    )

def todo_detail(request, seq):
    detail = Todo.objects.get(pk=seq)
    return render(request, "second/todo_detail.html", {
        'detail': detail
    })

def todo_register(request):
    if request.method == 'GET':
        form = TodoModelForm()
        return render(request, 'second/todo_register.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = TodoModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            return redirect("second:todo")
        else:
            return render(request, 'second/todo_register.html', {
                'form':form
            })

def favourite_modify(request, seq):
    
    favourite = Favourite.objects.get(pk=seq)

    if request.method == 'GET':
        form = FavouriteModelForm(instance=favourite)
        return render(request, 'second/favourite_modify.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = FavouriteModelForm(request.POST, instance=favourite)
        if form.is_valid():
            form.save() 
            return redirect("second:favourite")
        else:
            return render(request, 'second/favourite_register.html', {
                'form':form
            })

def favourite_delete(request, seq):
    favourite = Favourite.objects.get(pk=seq)

    favourite.delete()
    return redirect("second:favourite")


def todo_delete(request, seq):
    todo = Todo.objects.get(pk=seq)

    todo.delete()
    return redirect("second:todo")

def todo_modify(request, seq):
    
    todo = Todo.objects.get(pk=seq)

    if request.method == 'GET':
        form = TodoModelForm(instance=todo)
        return render(request, 'second/todo_modify.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            form.save() 
            return redirect("second:todo")
        else:
            return render(request, 'second/todo_register.html', {
                'form':form
            })
