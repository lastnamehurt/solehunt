from graphene_django import DjangoObjectType

from subscribers.models import Subscriber


class SubscriberType(DjangoObjectType):
    class Meta:
        model = Subscriber
        use_connection = True
        only_fields = (
            'id',
            'alias',
            'profile',
            'isActive',
            'isContributor'
        )
