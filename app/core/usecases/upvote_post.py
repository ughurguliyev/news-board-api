from stories import Success, Failure, Result, story, arguments


class UpvotePost:
    """Add Upvote to News Post Usecase"""

    @story
    @arguments("post_id")
    def apply(I):
        I.validate_inputs
        I.fetch_post
        I.upvote_post
        I.done

    def validate_inputs(self, ctx):
        if ctx.post_id:
            return Success()
        return Failure(reason="post_id_required")

    def fetch_post(self, ctx):
        ctx.post = self.news_repo.get_post(id=ctx.post_id)
        return Success() if ctx.post else Failure(reason="post_not_found")

    def upvote_post(self, ctx):
        ctx.updated_post = self.news_repo.upvote_post(post=ctx.post)
        return Success() if ctx.updated_post else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.updated_post)


UpvotePost.apply.failures(["post_id_required", "post_not_found", "repo_error"])
