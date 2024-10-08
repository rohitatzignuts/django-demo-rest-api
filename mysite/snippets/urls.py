from django.urls import path
from snippets import views

urlpatterns = [
    path("", views.snippetList, name="snippets-view-create"),
    path(
        "<int:pk>/",
        views.snippetDetails,
        name="snippet-retrive-update-destroy",
    ),
]
