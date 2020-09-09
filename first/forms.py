from django import forms
from .models import Students
import re

def check_address(value): #validator - 리스트 형태로 여러개 입력 가능.
    if len(value)<3 or bool(re.search('\s', value))==False:
        raise forms.ValidationError('적절한 주소 형태로 입력해주세요!')
def check_email(value): 
    if bool(re.match('[A-Za-z0-9_+\.,]+@[a-z\.]+',value))==False:
        raise forms.ValidationError('적절한 이메일 형식이 아닙니다!')

class StudentForms(forms.Form): #Django Form 
    name = forms.CharField(label='이름', max_length=10)
    address = forms.CharField(label='주소', validators=[check_address, ])
    email = forms.CharField(widget=forms.Textarea, validators=[check_email, ])

class StudentModelForms(forms.ModelForm):
    class Meta: #반드시 입력해야 한다!
        model = Students
        fields = '__all__' #전부다 입력