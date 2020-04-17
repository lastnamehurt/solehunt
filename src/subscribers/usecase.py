from core.usecases import BaseUseCase
from subscribers.services.subscriber_service import subscriberService


class CreateSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.createNewSubscriber


class UpdateSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.updateSubscriberById


class GetSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.getSubscriberById


class DeleteSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.deleteSubscriberById


class ActivateSubscriptionUseCase(BaseUseCase):
    serviceMethod = subscriberService.activateSubscription


class DeactivateSubscriptionUseCase(BaseUseCase):
    serviceMethod = subscriberService.deactivateSubscription