from sneaker_rack.services.sneaker_service import rackService
from sneaker_rack.services.sneaker_service import sneakerService
from subscribers.seed import subscriberSeeder

SNEAKER_DICT = {

    'brand': 'Nike',
    'color': 'Black',
    'size': '10',
    'style': 'Air Max'
}


class SneakerSeeder(object):

    def seedSneaker(self):
        return sneakerService.create(SNEAKER_DICT)


class SneakerRackSeeder(object):

    @classmethod
    def seedSneakerRack(cls):
        return rackService.create(filters={'subscriber': subscriberSeeder.seedSubscriber()})


sneakerSeeder = SneakerSeeder()
rackSeeder = SneakerRackSeeder()
