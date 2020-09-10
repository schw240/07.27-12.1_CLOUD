from django.shortcuts import render
from .models import Favourite, Todo


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