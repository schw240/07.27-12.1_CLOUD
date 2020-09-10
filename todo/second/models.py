from django.db import models

# Create your models here.
class FavouriteGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add=True)
    group = models.ForeignKey(FavouriteGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TodoGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)
    del_yn = models.BooleanField()

    def __str__(self):
        return self.name

class Todo(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    STATUS_CHOICES=(
    ('pending','할일'),
    ('inprogress','진행중'),
    ('end','완료')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    reg_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    del_yn = models.BooleanField()
    group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE)
