from django.test import TestCase
from sneaker_rack.services.sneaker_service import sneakerService, rackService
from sneaker_rack.seed import SNEAKER_DICT, sneakerSeeder


# Create your tests here.
class SneakerTest(TestCase):

    def setUp(self):
        # handles testCreateSneaker since it runs .create()
        self.sneaker = sneakerSeeder.seedSneaker()
        self.assertIsInstance(self.sneaker, sneakerService.repo.repo)
        self.assertEqual('Nike', self.sneaker.brand)
        self.assertEqual('Black', self.sneaker.color)
        self.assertEqual('10', self.sneaker.size)
        self.assertEqual('Air Max', self.sneaker.style)

    def testDeleteSneaker(self):
        sneakerService.delete(self.sneaker.id)

    def testUpdateSneaker(self):
        sneakerDict = SNEAKER_DICT.copy()
        sneakerDict['size'] = '12'
        sneakerService.update(self.sneaker.id, sneakerDict)
        import pdb;pdb.set_trace()
        self.assertEqual('Nike', self.sneaker.brand)
        self.assertEqual('Black', self.sneaker.color)
        self.assertEqual('12', self.sneaker.size)
        self.assertEqual('Air Max', self.sneaker.style)

    def testAddToRack(self):
        pass

    def testRemoveFromRack(self):
        pass


class SneakerRackTest(TestCase):

    def testCreateSneakerRack(self):
        pass

    def testCreateTopFiveSneakers(self):
        pass

    def testUpdateTopSneakers(self):
        pass

    def testUpdateSneakerRack(self):
        pass

    def testRefreshRack(self):
        pass
    def testGetAllSneakersInRack(self):
        pass
