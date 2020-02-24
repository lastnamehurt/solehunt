import json

from rest_framework.test import APIClient, APITestCase

from subscribers.models import Subscriber
from subscribers.services.subscriber_service import subscriberService


class SubscriberViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.newSubscriber = subscriberService.createNewSubscriber(alias='NewGuy')
        cls.res = cls.client.get('/api/subscribers/', follow=True)

    def testGetAllSubscribers(self):
        subscriberId = json.loads(self.res.content)[0]['id']

        self.assertEqual(subscriberId, 1)

    def testGetSubscriberById(self):
        subscriber = subscriberService.createNewSubscriber(alias='NewGuy')
        res = self.client.get('/api/subscribers/1', follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(subscriber, Subscriber)
        self.assertEqual(subscriber.alias, 'NewGuy')

    def testUpdateSubscriber(self):
        subscriber = self.client.put('/api/subscribers/1/', {'alias': 'notNewNoMo'})
        self.assertEqual(subscriber.status_code, 200)
        subscriber = self.client.get('/api/subscribers/1', follow=True)
        self.assertTrue(json.loads(subscriber.content)['alias'] == 'notNewNoMo')

    def testDeleteSubscriber(self):
        # get subscriber to ensure is in database
        subscriber = self.client.get('/api/subscribers/1', follow=True)
        self.assertEqual(subscriber.status_code, 200)

        # delete subscriber by id
        self.client.delete('/api/subscribers/1/')

        # make sure subscriber is now returning a 404
        subscriber = self.client.get('/api/subscribers/1', follow=True)
        self.assertEqual(subscriber.status_code, 404)

    def testCreateSubscriber(self):
        # clean subscribers
        Subscriber.objects.all().delete()
        newSubscriberData = self.client.post('/api/subscribers/', {'alias': 'test'})
        newSubscriber = subscriberService.repo.getById(newSubscriberData.data['id'])

        self.assertIsInstance(newSubscriber, Subscriber)
        self.assertTrue(newSubscriber.alias == 'test')
        self.assertEqual(Subscriber.objects.count(), 1)

    def testHomeView(self):
        response = self.client.get('/home')

        self.assertEqual(response.status_code, 200)
