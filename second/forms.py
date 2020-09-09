from django import forms
from .models import Favourite, FavouriteGroup, Todo, TodoGroup
import re

class FavouriteModelForms(forms.ModelForm):
    class Meta: #반드시 입력해야 한다!
        model = Favourite
        fields = '__all__' #전부다 입력
        labels = {
            'name':'명칭', 'url': 'URL', 'memo':'메모', 'group':'그룹'
        }

class TodoModelForms(forms.ModelForm):
    class Meta: #반드시 입력해야 한다!
        model = Todo
        fields = ['name', 'status', 'end_date', 'group']
        labels = {
            'name':'명칭', 'status':'상태', 'end_date':'종료일', 'group':'그룹'
        }