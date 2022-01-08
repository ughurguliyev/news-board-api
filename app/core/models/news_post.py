from django.db import models

from app.utils.base_model import BaseModel


class NewsPost(BaseModel):
    title = models.CharField(
        verbose_name="Title", max_length=300, null=True, blank=True
    )
    link = models.URLField(verbose_name="News link", null=True, blank=True)
    amount_of_upvotes = models.IntegerField(default=0)
    author_name = models.CharField(
        verbose_name="Name of author", max_length=200, null=True, blank=True
    )
    comments = models.ManyToManyField("core.Comment", related_name="news", blank=True)

    class Meta:
        verbose_name = "News post"
        verbose_name_plural = "News posts"

    def __str__(self) -> str:
        return self.title
