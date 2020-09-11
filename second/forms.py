from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #회원가입 창
from django.forms.widgets import HiddenInput
from .models import Favourite, FavouriteGroup, Todo, TodoGroup, User
import re

class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호확인'
        self.fields['username'].help_text = '필수입력. 30자 이내. 영숫자 및 @/./+/-/_만 허용'
        self.fields['password1'].help_text = '영숫자 혼용, 최소 8자리 이상'
        self.fields['password2'].help_text = ''
    # * -> 리스트 - 튜플 차이
    # ** -> 딕셔너리 - x=y형태로 딕셔너리
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'phone_number', 'profile']
        labels ={
            'username':'아이디',
            'email':'이메일',
            'phone_number':'휴대전화 번호',
            'profile':'프로필'
        }

class ChangeInfoForm(SignupForm): # id 등 중요한 정보는 수정 못하게...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호확인'
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        
    class Meta(SignupForm.Meta):
        model = User
        fields = ['username','email', 'phone_number', 'profile', 'password1', 'password2']
        labels = {
            'email':'이메일',
            'phone_number':'휴대전화 번호',
            'profile':'프로필'
        }
        widgets = {'username':forms.HiddenInput(),
        'password1':forms.HiddenInput(),
        'password2':forms.HiddenInput()
        }



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)
        pass

    class Meta(UserCreationForm.Meta):
        model=User
        fields = ['username', 'password']
        labels = {
            'username':'아이디',
            'password':'비밀번호'
        }


class FavouriteModelForms(forms.ModelForm):
    class Meta: #반드시 입력해야 한다!
        model = Favourite
        fields = ['name', 'url', 'memo', 'group']#전부다 입력
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
