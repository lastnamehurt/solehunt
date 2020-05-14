from core.usecases import UseCaseManager
from subscribers.seed import subscriberSeeder
from utils.helpers import FILTERS
from utils.helpers import LikeFilters
from posts.usecases import LikePostUseCase
from posts.usecases.posts_usecase import CreatePostUseCase


class PostSeeder:

    def seedPost(self, subscriber=None):
        filters = FILTERS.CREATE_POST
        if subscriber:
            filters['subscriber'] = subscriber
        return UseCaseManager(CreatePostUseCase, filters=FILTERS.CREATE_POST).execute()


class LikeSeeder:

    def seedLike(self, post=None, likedBy=None):
        filters = LikeFilters.LIKE_POST
        filters['post_id'] = post.id
        filters['likedBy_id'] = likedBy.id
        return UseCaseManager(LikePostUseCase, filters=filters).execute()


postSeeder = PostSeeder()
likeSeeder = LikeSeeder()
