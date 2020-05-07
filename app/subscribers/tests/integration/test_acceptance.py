"""
RULE: must follow SoleHunt IG or Twitter to be subscribed
"""
from unittest import TestCase
from unittest import skip

from core.usecases import UseCaseManager
from posts.seed import likeSeeder
from posts.services import postService
from posts.services.like_service import likeService
from posts.tests.test_post_usecases import PostFilters as POST_FILTERS
from posts.usecases.posts_usecase import CreatePostUseCase
from posts.usecases.posts_usecase import DeletePostUseCase
from posts.usecases.posts_usecase import GetLikesUseCase
from posts.usecases.posts_usecase import GetSubscriberByLikesUseCase
from posts.usecases.posts_usecase import LikePostUseCase
from posts.usecases.posts_usecase import LikesCountUseCase
from posts.usecases.posts_usecase import UndeletePostUseCase
from posts.usecases.posts_usecase import UnlikePostUseCase
from subscribers.seed import subscriberSeeder
from subscribers.services.subscriber_service import subscriberService
from subscribers.usecase import ActivateSubscriptionUseCase
from subscribers.usecase import CreateSubscriberSneakerUseCase
from subscribers.usecase import DeactivateSubscriptionUseCase
from subscribers.usecase import DeleteSubscriberSneakerUseCase
from subscribers.usecase import MarkAsFavoriteSneakerUseCase
from subscribers.usecase import UnmarkFavoriteSneakerUseCase
from subscribers.usecase import UpdateSubscriberSneakerUseCase
from utils.helpers import reloadObject

sneakerData = {'brand': 'Nike', 'size': '3', 'style': 'Air Max'}


class SubscriptionTest(TestCase):

    def setUp(self):
        self.subscriber = subscriberSeeder.seedSubscriber()
        self.subscriber.isActive = False
        self.subscriber.save()
        UseCaseManager(CreateSubscriberSneakerUseCase, modelId=self.subscriber.id, filters=sneakerData).execute()

        # add subscriber to post model
        self.postData = POST_FILTERS.CREATE_POST.copy()
        self.postData['subscriber'] = self.subscriber

        # remove hard-coded post_id since this creates a post
        del self.postData['post_id']

        # setup Post integration
        self.post = UseCaseManager(CreatePostUseCase, filters=self.postData).execute()
        self.postId = self.post.id

    def testSubscribe(self):
        UseCaseManager(ActivateSubscriptionUseCase, modelId=self.subscriber.id).execute()
        reloadObject(self.subscriber)
        self.assertEqual(self.subscriber.isActive, True)

    def testUnsubscribe(self):
        # first force to active state
        self.subscriber.isActive = True
        self.subscriber.save()
        UseCaseManager(DeactivateSubscriptionUseCase, modelId=self.subscriber.id).execute()
        reloadObject(self.subscriber)
        self.assertFalse(self.subscriber.isActive)

    def testCreateSneaker(self):
        self.assertEqual(self.subscriber.sneakers.count(), 1)

    def testUpdateSneaker(self):
        sneaker = self.subscriber.sneakers.first()
        sneakerDataCopy = sneakerData.copy()
        sneakerDataCopy['color'] = 'Blue'
        UseCaseManager(UpdateSubscriberSneakerUseCase, modelId=sneaker.id,
                       filters=sneakerDataCopy).execute()
        reloadObject(sneaker)
        self.assertEqual(sneaker.color, 'Blue')

    def testDeleteSneaker(self):
        sneaker = self.subscriber.sneakers.first()
        UseCaseManager(DeleteSubscriberSneakerUseCase, modelId=sneaker.id).execute()
        self.assertEqual(0, len(self.subscriber.sneakers.all()))

    def testMarkAsFavoriteSneaker(self):
        sneaker = self.subscriber.sneakers.first()
        UseCaseManager(MarkAsFavoriteSneakerUseCase, modelId=sneaker.id).execute()
        reloadObject(sneaker)
        self.assertTrue(sneaker.isFavorite)

    def testRemoveFavoriteSneaker(self):
        sneaker = self.subscriber.sneakers.first()
        UseCaseManager(UnmarkFavoriteSneakerUseCase, modelId=sneaker.id).execute()
        reloadObject(sneaker)
        self.assertFalse(sneaker.isFavorite)

    def testPostToWall(self):
        self.assertEqual(self.postData['subscriber'], self.post.subscriber)
        self.assertEqual(self.postData['title'], self.post.title)
        self.assertEqual(self.postData['body'], self.post.body)
        self.assertIsNotNone(self.post.timestamp)
        self.assertEqual(self.subscriber.posts.count(), 1)

    def testLikePost(self):
        UseCaseManager(LikePostUseCase, filters={'likedBy_id': self.subscriber.id, 'post_id': self.postId}).execute()
        like = likeService.getLikeByPostIdAndLikedById(self.postId, self.subscriber.id)

        self.assertEqual(self.subscriber.id, self.post.subscriber_id)
        self.assertEqual(self.post.id, like.post_id)

    def testUnlikePost(self):
        like = likeSeeder.seedLike()
        UseCaseManager(UnlikePostUseCase, modelId=like.id).execute()
        reloadObject(like)

        self.assertFalse(like.isActive)

    def testLikesCount(self):
        likeService.getAllObjects().delete()

        self.assertEqual(0, likeService.getAllObjects().count())

        like = likeSeeder.seedLike()
        UseCaseManager(LikesCountUseCase, modelId=like.post_id).execute()

        self.assertEqual(1, like.post.likes.count())

    def testGetSubscriberByLikeId(self):
        """
        Test Get Subscriber from given like
        """
        like = likeSeeder.seedLike()
        subscriber = UseCaseManager(GetSubscriberByLikesUseCase, modelId=like.id).execute()

        self.assertEqual(like.post.subscriber.id, subscriber.id)

    def testDeletePost(self):
        UseCaseManager(DeletePostUseCase, modelId=self.post.id).execute()
        reloadObject(self.post)

        self.assertFalse(self.post.isActive)

    def testUndeletePost(self):
        # delete post first
        postService.deletePost(self.post.id)
        reloadObject(self.post)

        self.assertFalse(self.post.isActive)

        # Un-delete
        UseCaseManager(UndeletePostUseCase, modelId=self.post.id).execute()
        reloadObject(self.post)

        self.assertTrue(self.post.isActive)

    def testViewBlogs(self):
        """
        A blog is a post from Ghost written by a contributor (Subscriber.isContributor)
        A Profile can_view_blogs
        """
        pass

    def testViewPosts(self):
        """
        A post is an internal post from Subscribers
        """
        pass

    def testManageFavoriteSneakers(self):
        """
        Manage top n sneakers
        """
        pass

    def testGetLikesForPost(self):
        # delete all likes
        likeService.getAllObjects().delete()
        # seed new like for test
        likeSeeder.seedLike()
        likes = UseCaseManager(GetLikesUseCase, filters={'post_id': 1, 'likedBy_id': 1}).execute()
        like = likes.first()

        self.assertEqual(1, likes.count())
        self.assertEqual(like.post_id, 1)
        self.assertEqual(like.likedBy_id, 1)
