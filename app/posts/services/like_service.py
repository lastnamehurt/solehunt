from core.core_service import SoleHuntBaseService
from posts.mappers.type_mapper import LikeSchema
from posts.repos.likes_repo import likesRepo


class LikeService(SoleHuntBaseService):
    repo = likesRepo

    @classmethod
    def likePost(cls, filters: LikeSchema.LIKE_POST) -> LikeSchema.LIKE_OBJECT:
        if not cls.repo.exists(filters):
            return cls.create(filters)
        return cls.repo.getByFilter(filters).first()

    @classmethod
    def unlikePost(cls, filters):
        postId = filters.get('id', None)
        return cls.update(postId, filters)

    @classmethod
    def getLikeCount(cls, postId):
        return cls.repo.query().filter(post_id=postId, isActive=True).count()

    @classmethod
    def getSubscriber(cls, modelId):
        return cls.repo.query().filter(id=modelId).values('subscriber')

    @classmethod
    def getPostByLikes(cls, modelId):
        return cls.repo.query().filter(postId=modelId).values('post')


likeService = LikeService()
