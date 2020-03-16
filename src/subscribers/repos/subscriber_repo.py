from core.base_repo import BaseRepo
from subscribers.models import Subscriber


class SubscriberRepo(BaseRepo):

    repo = Subscriber
