from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns(
    [
        path("", views.api_root),
        path("", views.SnippetList.as_view(), name="snippet-list"),
        path(
            "snippets/<int:pk>/highlight/",
            views.SnippetHighlight.as_view(),
            name="snippet-highlight",
        ),
        path("users/", views.UsersList.as_view(), name="user-list"),
        path(
            "<int:pk>/",
            views.SnippetDetails.as_view(),
            name="snippet-detail",
        ),
        path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    ]
)
