# Generated by Django 3.1.1 on 2020-09-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0003_todo_todogroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateField(),
        ),
    ]