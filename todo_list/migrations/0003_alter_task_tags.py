# Generated by Django 5.0.4 on 2024-04-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0002_alter_task_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(
                related_name="tags", to="todo_list.tag"
            ),
        ),
    ]
