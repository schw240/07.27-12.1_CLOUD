from django.contrib import admin
from .models import FavouriteGroup, Favourite, Todo, TodoGroup

# Register your models here.
@admin.register(FavouriteGroup)
class FavouriteGroupAdmin(admin.ModelAdmin):
    pass

@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    pass

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoGroup)
class TodoGroupAdmin(admin.ModelAdmin):
    pass