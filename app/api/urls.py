from django.urls import path

from . import views

urlpatterns = [
    path("post/create/", views.CreateNewsPostAPIView.as_view(), name="create_post"),
    path(
        "post/<pk>/",
        views.RetrieveUpdateDestroyNewsPostAPIView.as_view(),
        name="retrieve_update_destroy_post",
    ),
    path("post/<pk>/upvote/", views.UpvotePostAPIView.as_view(), name="upvote_post"),
    path(
        "post/<pk>/comment/create/",
        views.CreateCommentAPIView.as_view(),
        name="create_comment",
    ),
    path(
        "comment/<pk>/",
        views.RetrieveUpdateDestroyCommentAPIView.as_view(),
        name="retrieve_update_destroy_comment",
    ),
]
