from subscribers.services.subscriber_service import subscriberService
from core.usecase import BaseUseCase


class CreateSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.create


class UpdateSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.update


class GetSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.get


class DeleteSubscriberUseCase(BaseUseCase):
    serviceMethod = subscriberService.delete
