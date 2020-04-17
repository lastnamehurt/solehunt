"""
RULE: must follow SoleHunt IG or Twitter to be subscribed
"""
from unittest import TestCase

from core.usecases import UseCaseManager
from subscribers.seed import subscriberSeeder
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

    def testSubscribe(self):
        UseCaseManager(ActivateSubscriptionUseCase, modelId=self.subscriber.id).execute()
        reloadObject(self.subscriber)
        self.assertEqual(self.subscriber.isActive, True)

    def testUnsubscribe(self):
        # first force to active state
        self.subscriber.isActive = True
        self.subscriber.save()
        UseCaseManager(DeactivateSubscriptionUseCase, modelId=self.subscriber.id).execute()

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
        pass

    def testManageFavoriteSneakers(self):
        pass

    def testLikePost(self):
        pass

    def testViewBlogs(self):
        """
        A blog is a post from Ghost, written by a contributor
        """
        pass

    def testViewPosts(self):
        """
        A post is an internal post from Subscribers
        """
        pass
