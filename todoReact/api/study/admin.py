from django.contrib import admin
from .models import Students, Scores


# Register your models here.
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','address','email']

class ScoresAdmin(admin.ModelAdmin):
    list_display = ['name']