from core.usecases import BaseUseCase
from posts.services import postService


class CreatePostUseCase(BaseUseCase):
    serviceMethod = postService.create


class UpdatePostUseCase(BaseUseCase):
    serviceMethod = postService.update


class DeletePostUseCase(BaseUseCase):
    serviceMethod = postService.delete


class GetPostUseCase(BaseUseCase):
    serviceMethod = postService.get
