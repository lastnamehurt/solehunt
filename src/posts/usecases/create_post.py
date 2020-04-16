from core.usecase import BaseUseCase
from posts.services import postService


class CreatePost(BaseUseCase):

    serviceMethod = postService.create
