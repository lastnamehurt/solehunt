from core.core_service import SoleHuntBaseService
from posts.repos.post_repo import PostRepo


class PostService(SoleHuntBaseService):
    repo = PostRepo


postService = PostService()
