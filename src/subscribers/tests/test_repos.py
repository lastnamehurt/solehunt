from django.test import TestCase

from subscribers.models import Subscriber
from subscribers.repos.subscriber_repo import SubscriberRepo

first = {'alias': 'test', 'isActive': True}
second = {'alias': 'testGetById'}
third = {'alias': 'testGetByFilter'}


class SubscriberRepoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.repo = SubscriberRepo()
        cls.obj = cls.repo.create(first)
        cls.obj1 = cls.repo.create(second)
        cls.obj2 = cls.repo.create(third)

    def test_create(self):
        self.assertIsInstance(self.obj, Subscriber)
        self.assertTrue(self.obj.alias == 'test')
        self.assertTrue(self.obj.isActive)

    def testGetById(self):
        self.repo.getById(1)
        self.assertIsInstance(self.obj1, Subscriber)
        self.assertTrue(self.obj1.alias == 'testGetById')

    def testDelete(self):
        obj = self.repo.deleteById(1)
        self.assertNotIsInstance(obj, Subscriber)

    def testGetByFilter(self):
        obj = self.repo.getByFilter(alias='testGetByFilter')
        self.assertIsInstance(obj.first(), Subscriber)
        self.assertTrue(obj.first().alias == 'testGetByFilter')
