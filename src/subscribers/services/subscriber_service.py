from subscribers.repos.subscriber_repo import SubscriberRepo

class SubscriberService(object):

    repo = SubscriberRepo()

    def createNewSubscriber(self, **kwargs):
        subscriber = self.repo.create(**kwargs)
        if not subscriber.email:
            raise ValueError("Email Required")
