from django import forms

class StudentForms(forms.Form): #Django Form 
    name = forms.CharField()
    address = forms.CharField()
    email = forms.CharField(widget=forms.Textarea)
