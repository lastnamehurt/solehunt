from core.core_repo import BaseRepo
from sneaker_rack.models import Sneaker, SneakerRack


class SneakerRepo(BaseRepo):
    repo = Sneaker


class SneakerRackRepo(BaseRepo):
    repo = SneakerRack


sneakerRepo = SneakerRepo()
rackRepo = SneakerRackRepo()