from rest_framework import serializers

from core.models import NewsPost, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["updated_at"]


class NewsPostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = NewsPost
        exclude = ["updated_at"]
