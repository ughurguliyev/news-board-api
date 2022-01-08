from stories import Success, Failure, Result, story, arguments


class UpdateComment:
    @story
    @arguments("comment_id", "args")
    def apply(I):
        I.validate_inputs
        I.fetch_comment
        I.update_comment
        I.done

    def validate_inputs(self, ctx):
        if ctx.comment_id:
            return Success()
        return Failure(reason="comment_id_required")

    def fetch_comment(self, ctx):
        ctx.comment = self.news_repo.get_comment(id=ctx.comment_id)
        return Success() if ctx.comment else Failure(reason="comment_not_found")

    def update_comment(self, ctx):
        ctx.updated_comment = self.news_repo.update_comment(
            comment=ctx.comment,
            author_name=ctx.args.get("author_name"),
            content=ctx.args.get("content"),
        )
        return Success() if ctx.updated_comment else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.updated_comment)


UpdateComment.apply.failures(["comment_id_required", "comment_not_found", "repo_error"])
