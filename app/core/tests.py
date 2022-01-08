from django.test import TestCase

from core.implemented import (
    create_post,
    update_post,
    delete_post,
    create_comment,
    update_comment,
    delete_comment,
    upvote_post,
)


class NewsTestCase(TestCase):
    def setUp(self):
        self.post_args = {
            "title": "Demo",
            "link": "https://google.com",
            "amount_of_upvotes": 20,
            "author_name": "John Doe",
        }
        self.comment_args = {"author_name": "John Doe", "content": "Demo Content"}
        self.created_post = create_post.apply.run(
            title=self.post_args["title"],
            link=self.post_args["link"],
            amount_of_upvotes=self.post_args["amount_of_upvotes"],
            author_name=self.post_args["author_name"],
        )
        self.created_comment = create_comment.apply.run(
            post_id=self.created_post.value.id,
            author_name=self.comment_args["author_name"],
            content=self.comment_args["content"],
        )

    def test_created_post(self):
        self.assertEqual(self.created_post.is_success, True)
        self.assertEqual(self.created_post.value.title, self.post_args["title"])
        self.assertEqual(
            self.created_post.value.amount_of_upvotes,
            self.post_args["amount_of_upvotes"],
        )

    def test_updated_post(self):
        updated_post_args = {
            "title": "Demo 2",
            "link": "https://www.bbc.com/",
            "amount_of_upvotes": 10,
            "author_name": "John Doe 2",
        }
        updated_post = update_post.apply.run(
            post_id=self.created_post.value.id, args=updated_post_args
        )
        self.assertEqual(updated_post.is_success, True)
        self.assertEqual(updated_post.value.title, updated_post_args["title"])
        self.assertEqual(
            updated_post.value.amount_of_upvotes, updated_post_args["amount_of_upvotes"]
        )

    def test_deleted_post(self):
        deleted_post = delete_post.apply.run(post_id=self.created_post.value.id)
        self.assertEqual(deleted_post.is_success, True)

    def test_created_comment(self):
        self.assertEqual(self.created_comment.is_success, True)
        self.assertEqual(
            self.created_comment.value.author_name, self.comment_args["author_name"]
        )

    def test_updated_comment(self):
        updated_comment_args = {
            "author_name": "Jean Dupont",
            "content": "Demo Content 2",
        }
        updated_comment = update_comment.apply.run(
            comment_id=self.created_comment.value.id, args=updated_comment_args
        )
        self.assertEqual(updated_comment.is_success, True)
        self.assertEqual(updated_comment.value.content, updated_comment_args["content"])

    def test_deleted_comment(self):
        deleted_comment = delete_comment.apply.run(
            comment_id=self.created_comment.value.id
        )
        self.assertEqual(deleted_comment.is_success, True)

    def test_upvote_post(self):
        upvoted_post = upvote_post.apply.run(post_id=self.created_post.value.id)
        self.assertEqual(upvoted_post.is_success, True)
