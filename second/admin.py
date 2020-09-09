from django.contrib import admin
from .models import FavouriteGroup, Favourite, newproj, newprojGroup, TodoGroup, Todo

# Register your models here.
@admin.register(FavouriteGroup)
class FavouriteGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    pass

@admin.register(newprojGroup)
class newprojGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(newproj)
class newprojAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoGroup)
class TodoGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass