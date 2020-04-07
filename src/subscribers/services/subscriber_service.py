from subscribers.repos import subscriberRepo


class SubscriberService(object):

    @staticmethod
    def deleteSubscriberById(subscriberId):
        subscriberRepo.deleteById(subscriberId)

    @staticmethod
    def deleteSubscribersById(subscriberIds):
        for subscriberId in subscriberIds:
            subscriberRepo.deleteById(subscriberId)

    @staticmethod
    def updateSubscriberById(subscriberId, **kwargs):
        subscriberRepo.update(subscriberId, **kwargs)

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
    def createNewSubscriber(**kwargs):
        subscriber = subscriberRepo.create(**kwargs)
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


subscriberService = SubscriberService()
