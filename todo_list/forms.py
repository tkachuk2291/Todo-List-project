from django import forms

from todo_list.models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "content",
            "deadline",
            "is_done",
            "tags",
        )


class TagCreateForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
