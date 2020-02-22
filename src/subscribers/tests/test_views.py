import json

from django.test import TestCase
from django.test.client import Client

from subscribers.services.subscriber_service import subscriberService


class SubscriberViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.newSubscriber = subscriberService.createNewSubscriber(alias='NewGuy')
        cls.res = cls.client.get('/api/subscribers/', follow=True)

    def testGetAllSubscribers(self):
        self.assertEqual(len(json.loads(self.res.content)['results']), 1)

    def testGetSubscriberById(self):
        subscriber = subscriberService.createNewSubscriber(alias='NewGuy')
        res = self.client.get('/api/subscribers/1', follow=True)
        self.assertEqual(res.status_code, 200)

    def testDeleteSubscriber(self):
        pass

    def testUpdateSubscriber(self):
        pass

    def testHomeView(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)
