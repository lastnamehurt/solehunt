from core.usecases import BaseUseCase
from posts.services import postService
from posts.services.like_service import likeService


class CreatePostUseCase(BaseUseCase):
    serviceMethod = postService.create


class UpdatePostUseCase(BaseUseCase):
    serviceMethod = postService.editPost


class DeletePostUseCase(BaseUseCase):
    serviceMethod = postService.deletePost


class UndeletePostUseCase(BaseUseCase):
    serviceMethod = postService.undeletePost


class GetPostUseCase(BaseUseCase):
    serviceMethod = postService.get


class GetPostsUseCase(BaseUseCase):
    serviceMethod = postService.getAllObjects


class LikePostUseCase(BaseUseCase):
    serviceMethod = likeService.likePost


class UnlikePostUseCase(BaseUseCase):
    serviceMethod = likeService.unlikePost


class LikesCountUseCase(BaseUseCase):
    serviceMethod = likeService.getLikeCount


class GetSubscriberByLikesUseCase(BaseUseCase):
    serviceMethod = likeService.getSubscriberByLikeId


class GetLikesUseCase(BaseUseCase):
    serviceMethod = likeService.getAllObjects


class GetLikeUseCase(BaseUseCase):
    serviceMethod = likeService.get
