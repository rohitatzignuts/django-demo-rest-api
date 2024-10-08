from django.urls import path
from . import views

urlpatterns = [
    path("postlist/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),
    path(
        "postlist/<int:pk>",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="blogpost-retrive-update-destroy",
    ),
]
