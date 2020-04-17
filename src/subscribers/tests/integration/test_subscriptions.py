"""
RULE: must follow SoleHunt IG or Twitter to be subscribed
"""
from unittest import TestCase

from core.usecases import UseCaseManager
from subscribers.seed import subscriberSeeder
from subscribers.usecase import ActivateSubscriptionUseCase
from subscribers.usecase import DeactivateSubscriptionUseCase
from utils.helpers import reloadObject


class SubscriptionTest(TestCase):

    def setUp(self):
        self.subscriber = subscriberSeeder.seedSubscriber()
        self.subscriber.isActive = False
        self.subscriber.save()

    def testSubscribe(self):
        UseCaseManager(ActivateSubscriptionUseCase, modelId=self.subscriber.id).execute()
        reloadObject(self.subscriber)
        self.assertEqual(self.subscriber.isActive, True)

    def testUnsubscribe(self):
        # first force to active state
        self.subscriber.isActive = True
        self.subscriber.save()
        UseCaseManager(DeactivateSubscriptionUseCase, modelId=self.subscriber.id).execute()

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
