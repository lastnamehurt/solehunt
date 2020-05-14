from sneaker_rack.services.sneaker_service import rackService, sneakerService
from subscribers.seed import subscriberSeeder

SNEAKER_DICT = {

    'brand': 'Nike',
    'color': 'Black',
    'size': '10',
    'style': 'Air Max'
}


class SneakerSeeder(object):

    def seedSneaker(self, subscriber=None):
        SNEAKER_DICT['subscriber'] = subscriber
        return sneakerService.create(SNEAKER_DICT)


class SneakerRackSeeder(object):

    @classmethod
    def seedSneakerRack(cls, subscriber=None):
        return rackService.create(filters={'subscriber': subscriber})


sneakerSeeder = SneakerSeeder()
rackSeeder = SneakerRackSeeder()
