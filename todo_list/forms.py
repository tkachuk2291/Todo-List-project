from django import forms

from todo_list.models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "is_done",
            "tags",
        )
