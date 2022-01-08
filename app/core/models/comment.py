from django.db import models

from app.utils.base_model import BaseModel


class Comment(BaseModel):
    author_name = models.CharField(verbose_name="Author name", max_length=200)
    content = models.TextField(verbose_name="Content", null=True, blank=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return self.content
