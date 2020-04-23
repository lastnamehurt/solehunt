from graphene_django import DjangoObjectType

from subscribers.models import Sneaker


class SneakerType(DjangoObjectType):
    class Meta:
        model = Sneaker
        use_connection = True
