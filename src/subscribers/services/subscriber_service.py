from core.core_service import SoleHuntBaseService
from subscribers.repos import subscriberRepo


# TODO: churt refactor this service to inherit SoleHuntBaseService
class SubscriberService(SoleHuntBaseService):
    repo = subscriberRepo.model

    @staticmethod
    def deleteSubscriberById(subscriberId):
        subscriberRepo.deleteById(subscriberId)

    @staticmethod
    def deleteSubscribersById(subscriberIds):
        for subscriberId in subscriberIds:
            subscriberRepo.deleteById(subscriberId)

    @staticmethod
    def updateSubscriberById(subscriberId, filters):
        subscriberRepo.update(subscriberId, **filters)

    @staticmethod
    def updateSubscribersById(subscriberIds, **kwargs):
        for subscriberId in subscriberIds:
            subscriberRepo.update(subscriberId, **kwargs)

    @staticmethod
    def updateOrCreateSubscriber(**kwargs):
        return subscriberRepo.createOrUpdate(**kwargs)

    @staticmethod
    def getSubscriberById(subscriberId):
        return subscriberRepo.getById(subscriberId)

    @staticmethod
    def getAllSubscribers():
        return subscriberRepo.fetchAll()

    @staticmethod
    def createNewSubscriber(filters):
        subscriber = subscriberRepo.create(filters)
        if not subscriber.alias:
            raise ValueError("Email Required")
        return subscriber

    @staticmethod
    def getSubscribersByFilter(**kwargs):
        return subscriberRepo.query().filter(**kwargs)

    @staticmethod
    def activeSubscriberCount():
        return subscriberRepo.count(isActive=True)

    @staticmethod
    def allSubscribersCount():
        return subscriberRepo.query().all().count()

    @classmethod
    def activateSubscription(cls, subscriberId):
        subscriber = subscriberRepo.getById(subscriberId)
        subscriber.isActive = True
        subscriber.save()

    @classmethod
    def deactivateSubscription(cls, subscriberId):
        subscriber = subscriberRepo.getById(subscriberId)
        subscriber.isActive = False
        subscriber.save()


subscriberService = SubscriberService()
