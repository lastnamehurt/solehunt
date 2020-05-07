from core.usecases import UseCaseManager
from utils.helpers import FILTERS
from utils.helpers import LikeFilters
from posts.usecases import LikePostUseCase
from posts.usecases.posts_usecase import CreatePostUseCase


class PostSeeder:

    def seedPost(self):
        return UseCaseManager(CreatePostUseCase, filters=FILTERS.CREATE_POST).execute()


class LikeSeeder:

    def seedLike(self):
        return UseCaseManager(LikePostUseCase, filters=LikeFilters.LIKE_POST).execute()


postSeeder = PostSeeder()
likeSeeder = LikeSeeder()