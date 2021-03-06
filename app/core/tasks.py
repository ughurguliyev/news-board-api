from celery import Celery

from core.repository import NewsRepository

app = Celery()
news_repo = NewsRepository()


@app.task
def reset_post_upvotes_count():
    updated_posts = news_repo.reset_upvotes_count()
    return updated_posts
