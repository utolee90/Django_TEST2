from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Students, Scores

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

    elif request.method == 'POST':
        if request.POST['name'] != '':
            Students.objects.create(name=request.POST['name'],
            address=request.POST['address'],
            email=request.POST['email'])
        data = Students.objects.all()
        return render(request, 'first/students.html', {
            'students':data
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

def scores(request):
    if request.method == 'GET':
        scores = Scores.objects.all()
    
        return render(request, 'first/scores.html', {
            'scores' : scores
        })
    elif request.method == 'POST':
        data = Scores.objects.all()
        if request.POST['name'] != '':
            Scores.objects.create(name=request.POST['name'],
            math=request.POST['math'],
            english=request.POST['english'],
            science=request.POST['science'])
        else:
            pass
        
        
        
        return render(request, 'first/scores.html', {
            'scores' : data
        })
    
def scores_del(request, name):
    pass