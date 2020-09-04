from django.contrib import admin
from .models import Students, Scores


# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
    pass