from django.shortcuts import render, redirect
from .models import Favourite, FavouriteGroup, Todo, TodoGroup
from .forms import FavouriteModelForms, TodoModelForms


# Create your views here.
def index(request):
    return render(request, 'second/layout.html')

def favourites(request):
    favourites = Favourite.objects.all()

    return render(request, 'second/favourites.html', {
        'favourites': favourites
    })

def favourites_detail(request, idn):
    favourite = Favourite.objects.get(pk=idn)
    delid = f'del-favourite-{favourite.seq}'
    return render(request, 'second/favourites_detail.html', {
        'favourite': favourite,
        'delid': delid,
        'idn' : idn
    })

def favourites_add(request):
    form = FavouriteModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        return render(request, 'second/favourites_add.html', {
            'form':form, 
            'action':'등록'
        })

    elif request.method == 'POST':
        form = FavouriteModelForms(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('second:favourites')
        else:
            return render(request, 'second/favourites_add.html', {
                'form':form,
                'action':'등록',
            })

def favourites_modify(request, idn):
    favourite = Favourite.objects.get(seq=idn)
    
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = FavouriteModelForms(instance=favourite)
        return render(request, 'second/favourites_add.html', {
            'form':form,
            'action':'수정',
        })

    elif request.method == 'POST':
        form = FavouriteModelForms(request.POST, instance=favourite)
        action = '수정'
        if form.is_valid():
            post = form.save()
            return redirect('second:favourites')
        else:
            return render(request, 'second/favourites_add.html', {
                'form':form,
                'action':'수정',
            })

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
        

def todo(request):

    todos_pending = Todo.objects.filter(status='Pending')
    todos_inprogress = Todo.objects.filter(status='Inprogress')
    todos_end = Todo.objects.filter(status='End')

    return render(request, 'second/todos.html', {
        'todos_pending' : todos_pending,
        'todos_inprogress' : todos_inprogress,
        'todos_end' : todos_end
    })

def todo_detail(request, ids):
    todo = Todo.objects.get(pk=ids)
    delid = f'del-todo-{todo.seq}'
    return render(request, 'second/todo_detail.html', {
         'todo': todo,
         'delid': delid,
         'idn': ids
    })
    

def todo_add(request):
    form = TodoModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        return render(request, 'second/todo_add.html', {
            'form':form,
            'action':'등록'
        })

    elif request.method == 'POST':
        form = TodoModelForms(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('second:todos')
        else:
            return render(request, 'second/todo_add.html', {
                'form':form,
                'action':'등록'
            })

def todo_modify(request, ids):
    todo = Todo.objects.get(seq=ids)
    
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = TodoModelForms(instance=todo)
        return render(request, 'second/todo_add.html', {
            'form':form,
            'action':'수정'
        })

    elif request.method == 'POST':
        form = TodoModelForms(request.POST, instance=todo)
        if form.is_valid():
            post = form.save()
            return redirect('second:todos')
        else:
            return render(request, 'second/todo_add.html', {
                'form':form,
                'action':'수정'
            })

def todo_delete(request):
    if request.method == 'GET':
        return redirect('second:todos')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Todo.objects.get(pk=delpk)
        item.delete()
        return redirect('second:todos')

def todo_quick(request):
    if request.method == 'GET' and request.GET.get('del'):
        delpk = request.GET['del']
        item = Todo.objects.get(pk=delpk)
        item.delete()

def todo_shift(request):
    if request.method == 'GET' and request.GET.get('status') and request.GET.get('seq'):
        seq = request.GET['seq']
        status = request.GET['status']
        item = Todo.objects.get(pk=seq)
        item.status = status
        item.save()
