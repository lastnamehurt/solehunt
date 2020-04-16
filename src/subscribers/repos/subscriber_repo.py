from core.core_repo import BaseRepo
from subscribers.models import Subscriber


class SubscriberRepo(BaseRepo):

    model = Subscriber


subscriberRepo = SubscriberRepo()
