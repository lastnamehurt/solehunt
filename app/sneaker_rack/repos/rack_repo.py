from core.core_repo import BaseRepo
from sneaker_rack.models import Sneaker
from sneaker_rack.models import SneakerRack

"""
IMPORTANT IF YOU'D LIKE TO SAVE TIME
PLEASE FOLLOW THIS PATTERN TO CREATE THE CRUDs OF YOUR API
THE END
"""


class SneakerRepo(BaseRepo):
    model = Sneaker


class SneakerRackRepo(BaseRepo):
    model = SneakerRack


sneakerRepo = SneakerRepo()
rackRepo = SneakerRackRepo()
