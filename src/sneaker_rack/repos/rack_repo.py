from core.core_repo import BaseRepo
from sneaker_rack.models import Sneaker, SneakerRack

"""
IMPORTANT IF YOU'D LIKE TO SAVE TIME
PLEASE FOLLOW THIS PATTERN TO CREATE THE CRUDs OF YOUR API
THE END
"""


class SneakerRepo(BaseRepo):
    repo = Sneaker


class SneakerRackRepo(BaseRepo):
    repo = SneakerRack


sneakerRepo = SneakerRepo()
rackRepo = SneakerRackRepo()
