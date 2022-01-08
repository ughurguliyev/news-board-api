from stories import Success, Failure, Result, story, arguments


class DeletePost:
    """ Delete News Post Usecase """
    @story
    @arguments("post_id")
    def apply(I):
        I.validate_inputs
        I.fetch_post
        I.delete_post
        I.done

    def validate_inputs(self, ctx):
        if ctx.post_id:
            return Success()
        return Failure(reason="post_id_required")

    def fetch_post(self, ctx):
        ctx.post = self.news_repo.get_post(id=ctx.post_id)
        return Success() if ctx.post else Failure(reason="post_not_found")

    def delete_post(self, ctx):
        ctx.deleted_post = self.news_repo.delete_post(post=ctx.post)
        return Success() if ctx.deleted_post else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.deleted_post)


DeletePost.apply.failures(["post_id_required", "post_not_found", "repo_error"])
