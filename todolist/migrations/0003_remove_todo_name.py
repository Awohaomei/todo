# Generated by Django 2.2.2 on 2019-06-19 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='name',
        ),
    ]
