from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.serializers import NewsPostSerializer, CommentSerializer
from core.implemented import (
    create_post,
    update_post,
    delete_post,
    create_comment,
    update_comment,
    delete_comment,
    upvote_post,
)
from core.models import NewsPost, Comment
from api.decorators import handle_errors


class CreateNewsPostAPIView(APIView):
    serializer_class = NewsPostSerializer
    permission_classes = (permissions.AllowAny,)

    @handle_errors
    def post(self, request, *args, **kwargs):
        r = create_post.apply.run(
            title=request.data.get("title"),
            link=request.data.get("link"),
            amount_of_upvotes=request.data.get("amount_of_upvotes"),
            author_name=request.data.get("author_name"),
        )
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("not_validated"):
            result = "Data is not valid."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)


class RetrieveUpdateDestroyNewsPostAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = NewsPostSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = NewsPost.objects.all()

    @handle_errors
    def put(self, request, *args, **kwargs):
        r = update_post.apply.run(post_id=kwargs["pk"], args=request.data)
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("post_id_required"):
            result = "Post ID is required."

        elif r.failed_because("post_not_found"):
            result = "Post not found."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)

    @handle_errors
    def delete(self, request, *args, **kwargs):
        r = delete_post.apply.run(
            post_id=kwargs["pk"],
        )
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("post_id_required"):
            result = "Post ID is required."

        elif r.failed_because("post_not_found"):
            result = "Post not found."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)


class CreateCommentAPIView(APIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)

    @handle_errors
    def post(self, request, *args, **kwargs):
        r = create_comment.apply.run(
            post_id=self.kwargs["pk"],
            author_name=request.data.get("author_name"),
            content=request.data.get("content"),
        )
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("not_validated"):
            result = "Data is not valid."

        elif r.failed_because("post_not_found"):
            result = "Post not found."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)


class RetrieveUpdateDestroyCommentAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Comment.objects.all()

    @handle_errors
    def put(self, request, *args, **kwargs):
        r = update_comment.apply.run(comment_id=kwargs["pk"], args=request.data)
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("comment_id_required"):
            result = "Comment ID is required."

        elif r.failed_because("comment_not_found"):
            result = "Comment not found."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)

    @handle_errors
    def delete(self, request, *args, **kwargs):
        r = delete_comment.apply.run(
            comment_id=kwargs["pk"],
        )
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("comment_id_required"):
            result = "Comment ID is required."

        elif r.failed_because("comment_not_found"):
            result = "Comment not found."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)


class UpvotePostAPIView(APIView):
    serializer_class = NewsPostSerializer
    permission_classes = (permissions.AllowAny,)

    @handle_errors
    def post(self, request, *args, **kwargs):
        r = upvote_post.apply.run(post_id=kwargs["pk"])
        stat = status.HTTP_400_BAD_REQUEST
        success = False

        if r.is_success:
            success = True
            stat = status.HTTP_200_OK
            result = self.serializer_class(r.value).data

        elif r.failed_because("post_id_required"):
            result = "Post ID is required."

        elif r.failed_because("post_not_found"):
            result = "Post not found."

        elif r.failed_because("repo_error"):
            result = "Try again. Something went wrong."

        else:
            result = "Unexpected Error."

        return Response({"success": success, "result": result}, status=stat)
