from blog.services import blogService
from core.usecase import BaseUseCase


class CreateBlogUseCase(BaseUseCase):
    serviceMethod = blogService.create

class UpdateBlogUseCase(BaseUseCase):
    serviceMethod = blogService.update

class DeleteBlogUseCase(BaseUseCase):
    serviceMethod = blogService.delete

class GetBlogUseCase(BaseUseCase):
    serviceMethod = blogService.get

