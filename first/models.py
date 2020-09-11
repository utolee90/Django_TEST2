from django.db import models
from django import forms
from uuid import uuid4 #random id 생성
import os

# Create your models here.
def upload_to(instance, filename):
    path = 'file/'
    uuid_name = uuid4().hex
    #확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    #filename.split('.')[-1]
    return path + uuid_name + extension+'/'

class Students(models.Model):
    name=models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    file1 = models.FileField(null=True, blank=True, upload_to='')
    file2 = models.FileField(null=True, blank=True, upload_to=upload_to)
    image1 = models.ImageField(null=True, blank=True, upload_to='images/')
    image2 = models.ImageField(null=True, blank=True, upload_to='%Y/%m/%d')


class Scores(models.Model):
    name = models.CharField(max_length=10)
    math = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()
    