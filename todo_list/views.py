from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.forms import TaskCreateForm, TagCreateForm
from todo_list.models import Task, Tag


class HomeListView(generic.ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks_list"
    Task.is_done = False

    def get_queryset(self):
        return Task.objects.order_by("-is_done", "datetime")


class HomeCreateView(generic.CreateView):
    form_class = TaskCreateForm
    model = Task
    template_name = "task_create.html"
    context_object_name = "task_create"
    success_url = reverse_lazy("todo_list:home-page")


class HomeDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:home-page")


class HomeUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "task_create.html"
    context_object_name = "task_update"
    success_url = reverse_lazy("todo_list:home-page")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tags_list.html"
    context_object_name = "tag_list"


class TagsCreateView(generic.CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "tags_create.html"
    success_url = reverse_lazy("todo_list:tags")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "tags_create.html"
    context_object_name = "tag_update"
    success_url = reverse_lazy("todo_list:tags")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tags")


class StatusTask(View):
    model = Task
    success_url = reverse_lazy("todo_list:home-page")

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_list:home-page"))
