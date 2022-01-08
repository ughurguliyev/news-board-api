from stories import Success, Failure, Result, story, arguments


class DeleteComment:
    @story
    @arguments("comment_id")
    def apply(I):
        I.validate_inputs
        I.fetch_comment
        I.delete_comment
        I.done

    def validate_inputs(self, ctx):
        if ctx.comment_id:
            return Success()
        return Failure(reason="comment_id_required")

    def fetch_comment(self, ctx):
        ctx.comment = self.news_repo.get_comment(id=ctx.comment_id)
        return Success() if ctx.comment else Failure(reason="comment_not_found")

    def delete_comment(self, ctx):
        ctx.deleted_comment = self.news_repo.delete_comment(comment=ctx.comment)
        return Success() if ctx.deleted_comment else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.deleted_comment)


DeleteComment.apply.failures(["comment_id_required", "comment_not_found", "repo_error"])
