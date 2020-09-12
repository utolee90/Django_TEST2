from django.shortcuts import render, redirect
from .models import Favourite, FavouriteGroup, Todo, TodoGroup, User
from .forms import FavouriteModelForms, TodoModelForms, SignupForm, LoginForm, ChangeInfoForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'second/layout.html')

@login_required
def favourites(request):
    if request.method == 'GET':
        favourites = Favourite.objects.filter(user=request.user.username)

        return render(request, 'second/favourites.html', {
            'favourites': favourites
        })

@login_required
def favourites_detail(request, idn):
    favourite = Favourite.objects.get(pk=idn)
    delid = f'del-favourite-{favourite.seq}'
    favourites = Favourite.objects.filter(user=request.user.username)
    if favourite in favourites:
        return render(request, 'second/favourite_detail.html', {
            'favourite': favourite,
            'delid': delid,
            'idn' : idn
        })
    else:
        return render(request, 'second/noauth.html', {
            'action':'Favourite',
            'action_kr':'즐겨찾기가'
        })

@login_required
def favourites_add(request):
    form = FavouriteModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        return render(request, 'second/add.html', {
            'form':form, 
            'action':'등록',
            'do_action':'Add Favourite'
        })

    elif request.method == 'POST':
        form = FavouriteModelForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.POST['user']
            post.save()
            return redirect('second:favourites')
        else:
            return render(request, 'second/add.html', {
                'form':form,
                'action':'등록',
                'do_action':'Add Favourite'
            })

@login_required
def favourites_modify(request, idn):
    favourite = Favourite.objects.get(seq=idn)
    
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = FavouriteModelForms(instance=favourite)
        favourites = Favourite.objects.filter(user=request.user.username)
        if favourite in favourites:
            return render(request, 'second/add.html', {
                'form':form,
                'action':'수정',
                'do_action':'Modify Favourite',
            })
        else:
            return render(request, 'second/noauth.html', {
            'action':'Favourite',
            'action_kr':'즐겨찾기가'
            })


    elif request.method == 'POST':
        form = FavouriteModelForms(request.POST, instance=favourite)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.POST['user']
            post.save()
            return redirect('second:favourites')
        else:
            return render(request, 'second/add.html', {
                'form':form,
                'action':'수정',
                'do_action':'Modify Favourite',
            })

@login_required
def favourites_delete(request):
    if request.method == 'GET':
        return redirect('second:favourites')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Favourite.objects.get(pk=delpk)
        item.delete()
        return redirect('second:favourites')

def favourites_quick(request):
    if request.method == 'GET' and request.GET.get('del'):
        delpk = request.GET['del']
        item = Favourite.objects.get(pk=delpk)
        item.delete()
        
@login_required
def todo(request):

    todos_pending = Todo.objects.filter(status='Pending', user=request.user.username)
    todos_inprogress = Todo.objects.filter(status='Inprogress', user=request.user.username)
    todos_end = Todo.objects.filter( status='End', user=request.user.username)

    return render(request, 'second/todos.html', {
        'todos_pending' : todos_pending,
        'todos_inprogress' : todos_inprogress,
        'todos_end' : todos_end
    })

@login_required
def todo_detail(request, ids):
    todo = Todo.objects.get(pk=ids)
    delid = f'del-todo-{todo.seq}'
    todos = Todo.objects.filter(user=request.user.username)
    if todo in todos:
        return render(request, 'second/todo_detail.html', {
            'todo': todo,
            'delid': delid,
            'idn': ids
        })
    else:
        return render(request, 'second/noauth.html', {
            'action': 'Todo',
            'action_kr': '할일이'
        })
    
@login_required
def todo_add(request):
    form = TodoModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        return render(request, 'second/add.html', {
            'form':form,
            'action':'등록',
            'do_action':'Add Todo',
        })

    elif request.method == 'POST':
        form = TodoModelForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.POST['user']
            post.save()
            return redirect('second:todos')
        else:
            return render(request, 'second/add.html', {
                'form':form,
                'action':'등록',
                'do_action':'Add Todo',
            })

@login_required
def todo_modify(request, ids):
    todo = Todo.objects.get(seq=ids)
    
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = TodoModelForms(instance=todo)
        todos = Todo.objects.filter(user=request.user.username)
        if todo in todos:
            return render(request, 'second/add.html', {
                'form':form,
                'action':'수정',
                'do_action':'Modify Todo',
            })
        else:
            return render(request, 'second/noauth.html', {
            'action': 'Todo',
            'action_kr': '할일이'
        })


    elif request.method == 'POST':
        form = TodoModelForms(request.POST, instance=todo)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.POST['user']
            post.save()
            return redirect('second:todos'),
        else:
            return render(request, 'second/add.html', {
                'form':form,
                'action':'수정',
                'do_action':'Modify Todo',
            })

@login_required
def todo_delete(request):
    if request.method == 'GET':
        return redirect('second:todos')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Todo.objects.get(pk=delpk)
        item.delete()
        return redirect('second:todos')

@login_required
def todo_quick(request):
    if request.method == 'GET' and request.GET.get('del'):
        delpk = request.GET['del']
        item = Todo.objects.get(pk=delpk)
        item.delete()

@login_required
def todo_shift(request):
    if request.method == 'GET' and request.GET.get('status') and request.GET.get('seq'):
        seq = request.GET['seq']
        status = request.GET['status']
        item = Todo.objects.get(pk=seq)
        item.status = status
        item.save()

def signup(request):
    if request.method == 'GET':
        form=SignupForm()
        return render(request, "second/signup.html", {
            'form':form,
            'action':'회원가입'
        })
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            return redirect('second:index')
        else:
            return render(request, 'second/signup.html', {
                'form':form,
                'action' : '회원가입'
            })

def signin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "second/signup.html", {
            'form':form,
            'action':'로그인'
        })
    
    elif request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('second:index')
        else:
            return render(request, "second/signup.html", {
            'form':form,
            'action':'로그인'
        })

@login_required
def changeuserinfo(request):
    userinfo = User.objects.get(username=request.user.username)
    if request.method == 'GET':
        form=ChangeInfoForm(instance=userinfo)
        return render(request, "second/signup.html", {
            'form':form,
            'action':'회원정보수정'
        })
    elif request.method == 'POST':
        form = ChangeInfoForm(request.POST, instance=userinfo)
        if form.is_valid():
            signed_user = form.save()
            return redirect('second:index')
        else:
            return render(request, 'second/signup.html', {
                'form':form,
                'action' : '회원정보수정'
            })        

@login_required
def signout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('second:index')
