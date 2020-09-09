from django.contrib import admin
from .models import Students, Scores

# Register your models here.
@admin.register(Students)
@admin.register(Scores)
class StudentsAdmin(admin.ModelAdmin):
    pass
