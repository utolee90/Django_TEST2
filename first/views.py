from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from .models import Students, Scores
from .forms import StudentForms, StudentModelForms # import 하기

# Create your views here.
def index(request):
    # print(request.COOKIES)
    # request.session['userid'] = 'yohan'
    # del request.session['userid']  #세션 지울 때
    # request.session['count'] = '0' 
    return render(request, 'first/index.html')

def students(request):
    if request.method == 'GET':
        if request.GET.get('start') and request.GET.get('end'):
            start = int(request.GET['start'])
            end = int(request.GET['end'])
            students = Students.objects.filter(pk__range=(start, end))

        else:
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
    #form = StudentForms() #폼 객체 생성
    form = StudentModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        
        return render(request, 'first/students_add.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = StudentModelForms(request.POST, request.FILES) #파일 업로드할 때는 반드시 FILES도 입력!
        if form.is_valid():
            post = form.save()
            return redirect('first:students')
        else:
            return render(request, 'first/students_add.html', {
                'form':form
            })

def students_modify(request,id):
    try:
        student = Students.objects.get(pk=id)
    except:
        raise Http404("404")

    if request.method=='GET':
        form = StudentModelForms(instance=student) #instance값이 나옴.
        return render(request,'first/students_add.html',{
            'form':form})

    elif request.method=='POST':
        form = StudentModelForms(request.POST,instance=student)
        if form.is_valid():
            student=form.save()
            return render(request,'first/students_add.html',{
                'form':form})

def students_del(request):
    if request.method == 'GET':
        return redirect('first:students')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Students.objects.get(pk=delpk)
        delname = item.name
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
        
        return redirect('first:scores')


def scores_del(request):
    if request.method == 'GET':
        return redirect('first:scores')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Scores.objects.get(pk=delpk)
        delname = item.name
        item.delete()
        return render(request, 'first/scores_del.html', {
            'name':delname
        } )

def make_cookie(request, name):
    response = HttpResponse()
    response.set_cookie('name', name)
    return response

def get_cookie(request):
    pass
