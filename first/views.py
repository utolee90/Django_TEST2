from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Students, Scores
from .forms import StudentForms # import 하기

# Create your views here.
def index(request):
    
    return render(request, 'first/index.html')

def students(request):
    if request.method == 'GET':
        students = Students.objects.all()
        
        return render(request, 'first/students.html', {
            'text':'안녕하세요',
            'students': students
        })


def students_detail(request, id):
    print('id:', id)
    students = Students.objects.filter(pk=id)
    """
        SELECT * FROM students
        where pk=id 
    """
    return render(request, 'first/students.html', {
        'text':'안녕하세요',
        'students': students
    })

def students_add(request):
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = StudentForms() #폼 객체 생성
        return render(request, 'first/students_add.html', {
            'form':form
        })

    elif request.method == 'POST':
        if request.POST['name'] != '':
            Students.objects.create(name=request.POST['name'],
            address=request.POST['address'],
            email=request.POST['email'])
        return redirect('first:students')

def students_del(request):
    if request.method == 'GET':
        return redirect('first:students')
    
    elif request.method == 'POST':
        delname = request.POST['del']
        item = Students.objects.get(name=delname)
        item.delete()
        return render(request, 'first/students_del.html', {
            'name':delname
        } )

def scores(request):
    if request.method == 'GET':
        scores = Scores.objects.all()
        return render(request, 'first/scores.html', {
            'scores' : scores
        })

def scores_add(request):
    if request.method == 'GET':
        return render(request, 'first/scores_add.html')

    elif request.method == 'POST':
        if request.POST['name'] != '':
            Scores.objects.create(name=request.POST['name'],
            math=request.POST['math'],
            english=request.POST['english'],
            science=request.POST['science'])
        else:
            pass
        data = Scores.objects.all()
        return redirect('first:scores')


def scores_del(request):
    if request.method == 'GET':
        return redirect('first:scores')
    
    elif request.method == 'POST':
        delname = request.POST['del']
        item = Scores.objects.get(name=delname)
        item.delete()
        return render(request, 'first/scores_del.html', {
            'name':delname
        } )
