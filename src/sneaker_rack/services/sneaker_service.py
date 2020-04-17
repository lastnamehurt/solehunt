from core.core_service import SoleHuntBaseService
from sneaker_rack.repos import rackRepo
from sneaker_rack.repos import sneakerRepo
from utils.helpers import reloadObject


class SneakerService(SoleHuntBaseService):
    repo = sneakerRepo

    @classmethod
    def addToRack(cls, sneakerId: int, rackId: int) -> None:
        rackService.addSneaker(rackId, sneakerId)

    @classmethod
    def removeFromRack(cls, sneakerId):
        rackService.removeSneaker(sneakerId)

    @classmethod
    def makeFavorite(cls, sneakerId):
        cls.repo.update(sneakerId, {'isFavorite': True})

    @classmethod
    def removeFavorite(cls, sneakerId):
        cls.repo.update(sneakerId, {'isFavorite': False})


class SneakerRackService(SoleHuntBaseService):
    repo = rackRepo

    @classmethod
    def addSneaker(cls, rackId, sneakerId):
        """
        adds a sneaker to a given rack
        """
        rack = cls.get(rackId)
        sneaker = sneakerService.get(sneakerId)
        sneaker.rack = rack
        sneaker.save()

    @classmethod
    def removeSneaker(cls, sneakerId):
        sneaker = sneakerService.get(sneakerId)
        sneaker.rack = None
        sneaker.save()

    @classmethod
    def getSneakers(cls, subscriberId):
        """
        top n-sneakers
        """
        return sneakerService.getByFilters(filters={'subscriber_id': subscriberId})

    @classmethod
    def refreshRack(cls, rackId):
        rack = cls.get(rackId)
        return reloadObject(rack)


sneakerService = SneakerService()
rackService = SneakerRackService()
