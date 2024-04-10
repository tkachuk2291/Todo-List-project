from django.urls import path
from todo_list.views import HomeListView, HomeCreateView, HomeDeleteView, HomeUpdateView,StatusTask

urlpatterns = [
    path("", HomeListView.as_view(), name="home-page"),
    path("task-create/", HomeCreateView.as_view(), name="task-create"),
    path("task-delete/<int:pk>/", HomeDeleteView.as_view(), name="task-delete"),
    path("task-update/<int:pk>/", HomeUpdateView.as_view(), name="task-update"),
    path("task-status/<int:pk>/", StatusTask.as_view(), name="task-status"),


]
app_name = "todo_list"
