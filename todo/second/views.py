from django.shortcuts import render
from .models import Favourite, Todo

# Create your views here.
def index(request):
    return render(request, 'second/index.html')

def favourite(request):
    data = Favourite.objects.all()
    return render(request, "second/favourite.html",
        {'datas':data}
    )
def todo(request):

    pendings = Todo.objects.filter(status='pending')
    inprogress = Todo.objects.filter(status='inprogress')
    ends = Todo.objects.filter(status='end')

    return render(request, "second/todo.html",
        {
            'pendings':pendings,
            'inprogress':inprogress,
            'ends':ends
        }
    )

