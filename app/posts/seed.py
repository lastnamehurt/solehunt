from core.usecases import UseCaseManager
from subscribers.seed import subscriberSeeder
from utils.helpers import FILTERS
from utils.helpers import LikeFilters
from posts.usecases import LikePostUseCase
from posts.usecases.posts_usecase import CreatePostUseCase


class PostSeeder:

    def seedPost(self, seedSubscriber=True):
        subscriber = subscriberSeeder.seedSubscriber() if seedSubscriber else None
        filters = FILTERS.CREATE_POST
        if subscriber:
            filters['subscriber'] = subscriber
        return UseCaseManager(CreatePostUseCase, filters=FILTERS.CREATE_POST).execute()


class LikeSeeder:

    def seedLike(self):
        filters = LikeFilters.LIKE_POST
        post = postSeeder.seedPost()
        filters['post'] = post
        return UseCaseManager(LikePostUseCase, filters=filters).execute()


postSeeder = PostSeeder()
likeSeeder = LikeSeeder()
