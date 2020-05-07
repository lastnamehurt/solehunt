import logging

from core.core_service import SoleHuntBaseService
from posts.mappers.type_mapper import LikeSchema
from posts.repos.likes_repo import likesRepo

log = logging.getLogger(__name__)


class LikeService(SoleHuntBaseService):
    repo = likesRepo

    @classmethod
    def likePost(cls, filters) -> LikeSchema.LIKE_OBJECT:
        """
        each subscriber can like a post once
        filters = {'postId':1, 'likedBy_id':1}
        """

        # fetch Like
        likeQuery = cls.getByFilters(filters)

        # create Like if doesn't exist
        if not likeQuery:
            like = cls.create(filters)
        else:
            like = likeQuery.first()

        # if the post is not already likedBy the likedBy_id
        if not cls.isLiked(like.id):
            like.isActive = True
            like.save()

        return like

    @classmethod
    def unlikePost(cls, likeId):
        """
        unlike a given post by likeId
        """

        like = cls.get(likeId)

        if cls.isLiked(like.id):
            like.isActive = False
            like.save()
            log.info("Unliked Post {}".format(like.post_id))

    @classmethod
    def getLikeCount(cls, postId):
        return cls.repo.query().filter(post_id=postId, isActive=True).count()

    @classmethod
    def getSubscriberByLikeId(cls, likeId):
        return cls.get(likeId).post.subscriber

    @classmethod
    def getPostByLikeId(cls, likeId):
        return cls.get(likeId).post

    @classmethod
    def isLiked(cls, likeId):
        return cls.get(likeId).isActive

    @classmethod
    def getLikeByPostIdAndLikedById(cls, postId, likedById):
        filters = {'likedBy_id': likedById, 'post_id': postId}
        likeQuery = cls.getByFilters(filters)
        return likeQuery.first() if likeQuery else None

    @classmethod
    def getLikes(cls, filters):
        return cls.getByFilters(filters)

    @classmethod
    def getLikerFromLikedById(cls, likedById):
        possibleLikes = cls.getByFilters({'likedBy_id': likedById})
        if possibleLikes:
            return possibleLikes[0].likedBy


likeService = LikeService()
