# Generated by Django 3.2.9 on 2022-12-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0010_task_taskid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskId',
            field=models.IntegerField(verbose_name=models.AutoField(primary_key=True)),
        ),
    ]
