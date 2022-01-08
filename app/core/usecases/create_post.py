from stories import Success, Failure, Result, story, arguments


class CreatePost:
    """Create News Post Usecase"""

    @story
    @arguments("title", "link", "amount_of_upvotes", "author_name")
    def apply(I):
        I.validate_inputs
        I.create_post
        I.done

    def validate_inputs(self, ctx):
        if ctx.title and ctx.link and ctx.amount_of_upvotes and ctx.author_name:
            return Success()
        return Failure(reason="not_validated")

    def create_post(self, ctx):
        ctx.post = self.news_repo.create_post(
            title=ctx.title,
            link=ctx.link,
            amount_of_upvotes=ctx.amount_of_upvotes,
            author_name=ctx.author_name,
        )
        return Success() if ctx.post else Failure(reason="repo_error")

    def done(self, ctx):
        return Result(ctx.post)


CreatePost.apply.failures(["not_validated", "repo_error"])
