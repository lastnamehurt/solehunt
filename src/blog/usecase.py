from blog.services import blogService
from core.usecases import BaseUseCase


class CreateBlogUseCase(BaseUseCase):
    serviceMethod = blogService.createPost


class UpdateBlogUseCase(BaseUseCase):
    serviceMethod = blogService.updatePostById


class DeleteBlogUseCase(BaseUseCase):
    serviceMethod = blogService.deletePostById


class GetBlogUseCase(BaseUseCase):
    serviceMethod = blogService.getPostById
