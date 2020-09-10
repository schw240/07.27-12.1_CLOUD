from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from .models import Students, Scores
from .forms import StudentForm, StudentModelForm

# Create your views here.
@csrf_exempt
def index(request):
    print('한주', request.method)
    print('한주', request.GET)
    print('한주', request.headers)
    return render(request, 'first/index.html')

def students_detail(request, id):
    print("한번찍어보기", id)
    students = Students.objects.get(pk=id)
    return render(request, 'first/students_detail.html', {
        'student': students
    })
def students(request):
    """
    print('한주', request.method)
    print('한주', request.GET)
    print('한주', request.headers)
    """
    students = Students.objects.all()
    return render(request, 'first/students.html', {
        'text': 'Hello World! Hello World! Hello World!',
        'date': datetime.datetime.now,
        'students': students
    })

def scores(request):
    scores = Scores.objects.all()
    #render(request, 템플릿경로 TEXT, 보낼데이터 DICT
    return render(request, 'first/scores.html', {
        'scores':scores
    })

def scores_add(request):
    if request.method == 'GET':
        return render(request, 'first/scores_add.html')
    elif request.method == 'POST':
        Scores.objects.create(
            name=request.POST['name'],
            math=request.POST['math'],
            science=request.POST['science'],
            english=request.POST['english']
        )
        return redirect("first:scores")

def students_add(request):
    if request.method == 'GET':
        form = StudentModelForm()
        return render(request, 'first/students_add.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save()
            return redirect("first:students")
        else:
            return render(request, 'first/students_add.html', {
                'form':form
            })
        
        
        
        # if form.is_valid():
        #     #잘입력됬을경우
        #     Students.objects.create(
        #         name=form.cleaned_data['name'],
        #         address=form.cleaned_data['address'],
        #         email=form.cleaned_data['email']
        #     )
        #     return redirect("first:students")
        # else:
        #     return render(request, 'first/student_add.html', {
        #         'form':form
        #     })
        # Students.objects.create(
        #     name=request.POST['name'],
        #     address=request.POST['address'],
        #     email=request.POST['email']
        # )