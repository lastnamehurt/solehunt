import unittest

from django.test import TestCase

from subscribers.serializers import SubscriberSerializer
from subscribers.services.subscriber_service import subscriberService


@unittest.skip
class SubscriberSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.subscriber_attributes = {
            'alias': 'test1',
            'isActive': True
        }
        cls.subscriber = subscriberService.createNewSubscriber(**cls.subscriber_attributes)
        cls.serializer = SubscriberSerializer(instance=cls.subscriber)

    def testContainsExpectedFields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), {'id', 'alias', 'isActive', 'profile'})
