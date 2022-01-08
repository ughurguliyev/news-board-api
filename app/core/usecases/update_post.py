from stories import Success, Failure, Result, story, arguments


class UpdatePost:
    @story
    @arguments("post_id", "args")
    def apply(I):
        I.validate_inputs
        I.fetch_post
        I.update_post
        I.done

    def validate_inputs(self, ctx):
        if ctx.post_id:
            return Success()
        return Failure(reason="post_id_required")

    def fetch_post(self, ctx):
        ctx.post = self.news_repo.get_post(id=ctx.post_id)
        return Success() if ctx.post else Failure(reason="post_not_found")

    def update_post(self, ctx):
        ctx.updated_post = self.news_repo.update_post(
            post=ctx.post,
            title=ctx.args.get("title"),
            link=ctx.args.get("link"),
            amount_of_upvotes=ctx.args.get("amount_of_upvotes"),
            author_name=ctx.args.get("author_name"),
        )
        return Success() if ctx.updated_post else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.updated_post)


UpdatePost.apply.failures(["post_id_required", "post_not_found", "repo_error"])
