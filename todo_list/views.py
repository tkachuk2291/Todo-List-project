from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.forms import TaskCreateForm
from todo_list.models import Task


class HomeListView(generic.ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'tasks_list'
    Task.is_done = False
    def get_queryset(self):
        return Task.objects.order_by('-is_done', 'datetime')


class HomeCreateView(generic.CreateView):
    form_class = TaskCreateForm
    model = Task
    template_name = 'task_create.html'
    context_object_name = 'task_create'
    success_url = reverse_lazy("todo_list:home-page")


class HomeDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:home-page")


class HomeUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    context_object_name = 'task_update'
    # success_url = reverse_lazy("todo_list:home-page")


class StatusTask(View):
    model = Task
    success_url = reverse_lazy("todo_list:home-page")

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        if task.is_done is True:
            task.is_done = False
        else:
            task.is_done = True
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_list:home-page"))
