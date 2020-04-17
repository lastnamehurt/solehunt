from core.core_service import SoleHuntBaseService
from posts.repos.likes_repo import likesRepo


class LikesService(SoleHuntBaseService):
    repo = likesRepo

    @classmethod
    def likePost(cls, filters):
        return cls.create(filters)

likesService = LikesService()
