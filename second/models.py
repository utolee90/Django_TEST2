from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 기존 유저테이블이 아닌 새로 만들어야 한다.
class User(AbstractUser): #사용자 정보 추가 (사용자 처리는 전담.)
    phone_number=models.CharField(max_length=20, blank=True)
    profile = models.ImageField(verbose_name='user\'s profile image', null=True, blank=True, upload_to='second/profiles/')

class FavouriteGroup(models.Model):
    seq = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    seq = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add = True)
    user = models.CharField(max_length=30, default='AnonymousUser')
    group = models.ForeignKey(FavouriteGroup, on_delete = models.CASCADE)
    
class newprojGroup(models.Model):
    seq = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class newproj(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    reg_date = models.DateField(auto_now_add=False)
    end_date = models.DateField()
    del_yn = models.BooleanField(default=False)
    group = models.ForeignKey(newprojGroup, on_delete=models.CASCADE) 

class TodoGroup(models.Model):
    seq = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATUS_LIST=[
        ('Pending', '할일'),
        ('Inprogress', '진행중'),
        ('End', '완료'), 
    ]
    seq = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_LIST)
    reg_date = models.DateField(auto_now_add = True)
    end_date = models.DateField()
    del_yn = models.BooleanField(default=False)
    user = models.CharField(max_length=30, default='AnonymousUser')
    group = models.ForeignKey(TodoGroup, on_delete = models.CASCADE)

