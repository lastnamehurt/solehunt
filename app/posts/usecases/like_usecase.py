from core.usecases import BaseUseCase
from posts.services.like_service import likeService


class LikePostUseCase(BaseUseCase):
    serviceMethod = likeService.likePost


class UnlikePostUseCase(BaseUseCase):
    serviceMethod = likeService.unlikePost


class LikeCountUseCase(BaseUseCase):
    serviceMethod = likeService.getLikeCount


class GetPostByLikeUseCase(BaseUseCase):
    serviceMethod = likeService.getPostByLikeId


class GetSubscriberByLikeUseCase(BaseUseCase):
    serviceMethod = likeService.getSubscriberByLikeId
