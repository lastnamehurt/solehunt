from core.core_repo import BaseRepo
from posts.models import Post


class PostRepo(BaseRepo):
    model = Post


postRepo = PostRepo()
