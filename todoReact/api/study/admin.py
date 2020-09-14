from django.contrib import admin
from .models import Students, Scores


# Register your models here.
@admin.register(Students)
class StutentsAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
    list_display = ['name']