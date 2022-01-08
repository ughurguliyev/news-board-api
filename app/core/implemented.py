from core.usecases import (
    CreatePost,
    UpdatePost,
    DeletePost,
    CreateComment,
    UpdateComment,
    DeleteComment,
    UpvotePost,
)
from core.repository import NewsRepository

news_repo = NewsRepository()

# Usecase 1: Create News Post
create_post = CreatePost()
create_post.news_repo = news_repo

# Usecase 2: Update News Post
update_post = UpdatePost()
update_post.news_repo = news_repo

# Usecase 3: Delete News Post
delete_post = DeletePost()
delete_post.news_repo = news_repo

# Usecase 4: Create Comment
create_comment = CreateComment()
create_comment.news_repo = news_repo

# Usecase 5: Update Comment
update_comment = UpdateComment()
update_comment.news_repo = news_repo

# Usecase 6: Delete Comment
delete_comment = DeleteComment()
delete_comment.news_repo = news_repo

# Usecase 7: Upvote Post
upvote_post = UpvotePost()
upvote_post.news_repo = news_repo
