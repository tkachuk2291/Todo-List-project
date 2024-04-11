from django.urls import path
from todo_list.views import (
    HomeListView,
    HomeCreateView,
    HomeDeleteView,
    HomeUpdateView,
    StatusTask,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", HomeListView.as_view(), name="home-page"),
    path("task-create/", HomeCreateView.as_view(), name="task-create"),
    path(
        "task-delete/<int:pk>/", HomeDeleteView.as_view(), name="task-delete"
    ),
    path(
        "task-update/<int:pk>/", HomeUpdateView.as_view(), name="task-update"
    ),
    path("task-status/<int:pk>/", StatusTask.as_view(), name="task-status"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags-create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags-update/<int:pk>/", TagsUpdateView.as_view(), name="tag-update"),
    path("tag-delete/<int:pk>/", TagsDeleteView.as_view(), name="tag-delete"),
]
app_name = "todo_list"
