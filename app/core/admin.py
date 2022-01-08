from django.contrib import admin

from core.models import NewsPost, Comment

# Register your models here.


@admin.register(NewsPost)
class NewsPostAmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
