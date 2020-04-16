from subscribers.services.subscriber_service import subscriberService

SUBSCRIBER_DICT = {
    'alias': 'SoleHunt',
    'isActive': True,
}


class SubscriberSeeder(object):

    def seedSubscriber(self):
        return subscriberService.createNewSubscriber(filters=SUBSCRIBER_DICT)


subscriberSeeder = SubscriberSeeder()
