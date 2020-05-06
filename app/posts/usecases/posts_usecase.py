from core.usecases import BaseUseCase
from posts.services import postService
from posts.services.likes_service import likeService


class CreatePostUseCase(BaseUseCase):
    serviceMethod = postService.create


class UpdatePostUseCase(BaseUseCase):
    serviceMethod = postService.update


class DeletePostUseCase(BaseUseCase):
    serviceMethod = postService.delete


class GetPostUseCase(BaseUseCase):
    serviceMethod = postService.get


class LikePostUseCase(BaseUseCase):
    filters = {'isActive': True}
    serviceMethod = likeService.likePost


class UnlikePostUseCase(BaseUseCase):
    filters = {'isActive': False}
    serviceMethod = likeService.unlikePost


class LikesCountUseCase(BaseUseCase):
    serviceMethod = likeService.getLikeCount


class GetSubscriberByLikesUseCase(BaseUseCase):
    serviceMethod = likeService.getSubscriber
