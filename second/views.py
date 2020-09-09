from django.shortcuts import render
from .models import Favourite, FavouriteGroup, Todo, TodoGroup


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
        #'todos': todos
        'todos_pending' : todos_pending,
        'todos_inprogress' : todos_inprogress,
        'todos_end' : todos_end
    })

def todo_detail(request, idn):
    todo = Todo.objects.filter(pk=idn)
    return render(request, 'second/todo_detail.html', {
        'todo': todo[0]
    })


