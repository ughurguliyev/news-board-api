from core.models import NewsPost, Comment


class NewsRepository:
    def create_post(
        self, title: str, link: str, amount_of_upvotes: int, author_name: str
    ) -> NewsPost:
        new_post = NewsPost.objects.create(
            title=title,
            link=link,
            amount_of_upvotes=amount_of_upvotes,
            author_name=author_name,
        )
        return new_post

    def create_comment(self, post: NewsPost, author_name: str, content: str) -> Comment:
        new_comment = Comment.objects.create(author_name=author_name, content=content)
        post.comments.add(new_comment)
        return new_comment

    def get_post(self, id: str) -> NewsPost:
        return NewsPost.objects.filter(id=id).first()

    def get_comment(self, id: str) -> Comment:
        return Comment.objects.filter(id=id).first()

    def update_post(self, post: NewsPost, **kwargs):
        for key, value in kwargs.items():
            if value:
                if hasattr(post, key):
                    setattr(post, key, value)
        post.save()
        return post

    def update_comment(self, comment: Comment, **kwargs):
        for key, value in kwargs.items():
            if value:
                if hasattr(comment, key):
                    setattr(comment, key, value)
        comment.save()
        return comment

    def delete_post(self, post: NewsPost):
        post.delete()
        return post

    def reset_upvotes_count(self):
        count = NewsPost.objects.update(amount_of_upvotes=0)
        return count

    def upvote_post(self, post: NewsPost):
        post.amount_of_upvotes += 1
        post.save()
        return post

    def delete_comment(self, comment: Comment):
        comment.delete()
        return comment
