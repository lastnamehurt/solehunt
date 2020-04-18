from core.core_service import SoleHuntBaseService
from posts.repos.post_repo import PostRepo
from posts.services.likes_service import likesService


class PostService(SoleHuntBaseService):
    repo = PostRepo

    @classmethod
    def getLikes(cls, postId):
        return likesService.getByFilters({
            'post_id': postId
        })


postService = PostService()
