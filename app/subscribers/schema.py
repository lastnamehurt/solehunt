import graphene
from graphene_django.types import DjangoObjectType

from subscribers.services.subscriber_service import subscriberService


class SubscriberType(DjangoObjectType):
    class Meta:
        model = subscriberService.repo.model
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
        return subscriberService.getAllObjects()

    def resolve_subscriber(self, info, **kwargs):
        subscriberId = kwargs.get('id', None)
        if subscriberId is not None:
            return subscriberService.get(subscriberId)
