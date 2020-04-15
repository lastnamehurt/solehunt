from core.core_service import SoleHuntBaseService
from sneaker_rack.repos import rackRepo, sneakerRepo


class SneakerService(SoleHuntBaseService):

    repo = sneakerRepo

    def addToRack(self):
        pass

    def removeFromRack(self):
        pass



class SneakerRackService(SoleHuntBaseService):

    repo = rackRepo

    def createFavoriteSneakersList(self):
        pass

    def deleteFavoriteSneakersList(self):
        pass

    def refreshRack(self):
        pass


sneakerService = SneakerService()
rackService = SneakerRackService()