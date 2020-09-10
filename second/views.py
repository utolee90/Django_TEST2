from django.shortcuts import render, redirect
from .models import Favourite, FavouriteGroup, Todo, TodoGroup
from .forms import FavouriteModelForms, TodoModelForms


# Create your views here.
def index(request):
    return render(request, 'second/layout.html')

def favourites(request):
    favourites = Favourite.objects.all()
    """
        SELECT * 
            FROM favourite
    """

    return render(request, 'second/favourites.html', {
        'favourites': favourites
    })

def favourites_detail(request, idn):
    favourite = Favourite.objects.filter(pk=idn)
    
    return render(request, 'second/favourites_detail.html', {
        'favourite': favourite[0]
    })

def favourites_add(request):
    form = FavouriteModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        return render(request, 'second/favourites_add.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = FavouriteModelForms(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('second:favourites')
        else:
            return render(request, 'second/favourites_add.html', {
                'form':form
            })

def favourites_modify(request, idn):
    favourite = Favourite.objects.get(seq=idn)
    
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = FavouriteModelForms(instance=favourite)
        return render(request, 'second/favourites_add.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = FavouriteModelForms(request.POST, instance=favourite)
        if form.is_valid():
            post = form.save()
            return redirect('second:favourites')
        else:
            return render(request, 'second/favourites_add.html', {
                'form':form
            })

def favourites_delete(request):
    if request.method == 'GET':
        return redirect('second:favourites')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Favourite.objects.get(pk=delpk)
        item.delete()
        return redirect('second:favourites')

def todo(request):
    # group1= request.GET.get('group') #숫자 얻기
    # end_date1 = request.GET.get('end_date')
    # if group1 !=None:
    #     group_item = TodoGroup.objects.get(name=group1)
    #     groupnum = group_item.seq #숫자를 얻는다.
    # else:
    #     groupnum = None

    # if groupnum !=None:
    #     if end_date1 !=None:
    #         todos = Todo.objects.filter(group=groupnum, end_date__gte=end_date1)
    #     else:
    #         todos = Todo.objects.filter(group=groupnum)
    # else:
    #     if end_date1 !=None:
    #         todos = Todo.objects.filter(end_date__gte=end_date1)
    #     else:
    #         todos = Todo.objects.all()

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
    return render(request, 'second/todo_detail.html', {
         'todo': todo,
    })
    

def todo_add(request):
    form = TodoModelForms()
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        return render(request, 'second/todo_add.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = TodoModelForms(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('second:todos')
        else:
            return render(request, 'second/todo_add.html', {
                'form':form
            })

def todo_modify(request, ids):
    todo = Todo.objects.get(seq=ids)
    
    if request.method == 'GET': #get 메소드로 얻을 때는 강제
        form = TodoModelForms(instance=todo)
        return render(request, 'second/todo_add.html', {
            'form':form
        })

    elif request.method == 'POST':
        form = TodoModelForms(request.POST, instance=todo)
        if form.is_valid():
            post = form.save()
            return redirect('second:todos')
        else:
            return render(request, 'second/todo_add.html', {
                'form':form
            })

def todo_delete(request):
    if request.method == 'GET':
        return redirect('second:todos')
    
    elif request.method == 'POST':
        delpk = request.POST['del']
        item = Todo.objects.get(pk=delpk)
        item.delete()
        return redirect('second:todos')
