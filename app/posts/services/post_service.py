from core.core_service import SoleHuntBaseService
from posts.repos.post_repo import PostRepo


class PostService(SoleHuntBaseService):
    repo = PostRepo

    @classmethod
    def deletePost(cls, postId):
        cls.update(postId, {'isActive': False})

    @classmethod
    def undeletePost(cls, postId):
        cls.update(postId, {'isActive': True})

    @classmethod
    def editPost(cls, postId, filters):
        cls.update(postId, filters)


postService = PostService()
