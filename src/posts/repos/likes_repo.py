from core.core_repo import BaseRepo
from posts.models import Like


class LikesRepo(BaseRepo):
    model = Like


likesRepo = LikesRepo()
