from core.core_repo import BaseRepo
from subscribers.models import Subscriber


class SubscriberRepo(BaseRepo):

    repo = Subscriber


subscriberRepo = SubscriberRepo()
