from unittest.mock import patch

from django.test import TestCase

from sneaker_rack.seed import SNEAKER_DICT, rackSeeder, sneakerSeeder
from sneaker_rack.services.sneaker_service import rackService, sneakerService
# Create your tests here.
from subscribers.services.subscriber_service import subscriberService
from utils.helpers import reloadObject

RACK_ID = 1


class SneakerTest(TestCase):

    def setUp(self):
        self.sneaker = sneakerSeeder.seedSneaker()

    def testCreateSneaker(self):
        self.assertIsInstance(self.sneaker, sneakerService.repo.model)
        self.assertEqual('Nike', self.sneaker.brand)
        self.assertEqual('Black', self.sneaker.color)
        self.assertEqual('10', self.sneaker.size)
        self.assertEqual('Air Max', self.sneaker.style)

    def testDeleteSneaker(self):
        sneakerService.delete(self.sneaker.id)

    def testUpdateSneaker(self):
        sneakerDict = SNEAKER_DICT.copy()
        sneakerDict['size'] = '12'
        sneakerDict['color'] = 'Navy'
        sneakerService.update(self.sneaker.id, sneakerDict)
        reloadObject(self.sneaker)
        self.assertEqual('Nike', self.sneaker.brand)
        self.assertEqual('Navy', self.sneaker.color)
        self.assertEqual('12', self.sneaker.size)
        self.assertEqual('Air Max', self.sneaker.style)

    @patch('sneaker_rack.services.sneaker_service.SneakerRackService.addSneaker')
    def testAddToRack(self, mockAddSneaker):
        sneakerService.addToRack(self.sneaker.id, RACK_ID)
        self.assertTrue(mockAddSneaker.called)
        mockAddSneaker.assert_called_once()
        mockAddSneaker.assert_called_once_with(self.sneaker.id, RACK_ID)

    @patch('sneaker_rack.services.sneaker_service.SneakerRackService.removeSneaker')
    def testRemoveFromRack(self, mockRemoveSneaker):
        sneakerService.removeFromRack(self.sneaker.id)
        mockRemoveSneaker.assert_called_once()
        mockRemoveSneaker.assert_called_with(self.sneaker.id)

    @patch('core.core_repo.BaseRepo.update')
    def testAddFavorite(self, mockUpdate):
        sneakerService.makeFavorite(self.sneaker.id)
        mockUpdate.assert_called()

    @patch('core.core_repo.BaseRepo.update')
    def testRemoveFavorite(self, mockUpdate):
        sneakerService.removeFavorite(self.sneaker.id)
        mockUpdate.assert_called()


class SneakerRackTest(TestCase):

    def setUp(self):
        self.rack = rackSeeder.seedSneakerRack()
        self.SUBSCRIBER_ID = 1

    def testCreateSneakerRack(self):
        self.assertIsInstance(self.rack, rackService.repo.model)
        self.assertEqual(self.rack.subscriber, subscriberService.getSubscriberById(self.SUBSCRIBER_ID))

    @patch('core.core_service.SoleHuntBaseService.getByFilters')
    def testGetSneakers(self, mockGet):
        rackService.getSneakers(self.SUBSCRIBER_ID)

        mockGet.assert_called_once()
        mockGet.assert_called_with(filters={'subscriber_id': 1})

    @patch('django.db.models.base.Model.refresh_from_db')
    def testRefreshRack(self, mockReload):
        rackService.refreshRack(self.rack.id)

        mockReload.assert_called()

    @patch('core.core_service.SoleHuntBaseService.getByFilters')
    def testGetAllSneakersInRack(self, mockGet):
        rackService.getSneakers(self.SUBSCRIBER_ID)

        mockGet.assert_called_once()
        mockGet.assert_called_with(filters={'subscriber_id': self.SUBSCRIBER_ID})
