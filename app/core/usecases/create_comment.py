from stories import Success, Failure, Result, story, arguments


class CreateComment:
    """Create Comment Usecase"""

    @story
    @arguments("post_id", "author_name", "content")
    def apply(I):
        I.validate_inputs
        I.fetch_post
        I.create_comment
        I.done

    def validate_inputs(self, ctx):
        if ctx.post_id and ctx.author_name and ctx.content:
            return Success()
        return Failure(reason="not_validated")

    def fetch_post(self, ctx):
        ctx.post = self.news_repo.get_post(id=ctx.post_id)
        return Success() if ctx.post else Failure(reason="post_not_found")

    def create_comment(self, ctx):
        ctx.comment = self.news_repo.create_comment(
            post=ctx.post, author_name=ctx.author_name, content=ctx.content
        )
        return Success() if ctx.post else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.comment)


CreateComment.apply.failures(["not_validated", "post_not_found", "repo_error"])
