from core.usecases import BaseUseCase
from posts.services import postService
from posts.services.likes_service import likesService


class CreatePostUseCase(BaseUseCase):
    serviceMethod = postService.create


class UpdatePostUseCase(BaseUseCase):
    serviceMethod = postService.update


class DeletePostUseCase(BaseUseCase):
    serviceMethod = postService.delete


class GetPostUseCase(BaseUseCase):
    serviceMethod = postService.get


class LikePostUseCase(BaseUseCase):
    serviceMethod = likesService.likePost