from core.core_service import SoleHuntBaseService
from sneaker_rack.repos import rackRepo, sneakerRepo


class SneakerService(SoleHuntBaseService):

    repo = sneakerRepo

    def addToFavorites(self):
        pass

    def removeFromFavorites(self):
        pass

    def refreshFavorites(self):
        pass


class SneakerRackService(SoleHuntBaseService):

    repo = rackRepo

    def createFavoriteSneakersList(self):
        pass

    def deleteFavoriteSneakersList(self):
        pass
