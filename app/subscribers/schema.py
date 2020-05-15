import graphene
from graphene_django.types import DjangoObjectType

from core import UseCaseManager as useCaseManager
from subscribers.models import Subscriber
from subscribers.usecase import GetSubscriberUseCase
from subscribers.usecase import GetSubscribersUseCase


class SubscriberType(DjangoObjectType):
    class Meta:
        model = Subscriber
        fields = '__all__'


class Query(object):
    all_subscribers = graphene.List(SubscriberType)
    subscriber = graphene.Field(SubscriberType,
                                id=graphene.Int(),
                                alias=graphene.String(),
                                isActive=graphene.Boolean(),
                                isContributor=graphene.Boolean()
                                )

    def resolve_all_subscribers(self, info, **kwargs):
        return useCaseManager(GetSubscribersUseCase).execute()

    def resolve_subscriber(self, info, **kwargs):
        subscriberId = kwargs.get('id', None)
        if subscriberId is not None:
            return useCaseManager(GetSubscriberUseCase, modelId=subscriberId).execute()
