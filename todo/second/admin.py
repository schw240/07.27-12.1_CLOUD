from django.contrib import admin
from .models import FavouriteGroup

# Register your models here.
@admin.register(FavouriteGroup)
class FavouriteGroupAdmin(admin.ModelAdmin):
    pass