# from graphene import Argument
# from graphene import Field
# from graphene import ID
# from graphene import ObjectType
# from graphene import Schema
# from graphene_django import DjangoConnectionField
#
# from sneaker_rack.models import Sneaker
# from subscribers.models import Subscriber
# from .sneakers.types import SneakerType
# from .subscribers.types import SubscriberType
#
#
# class Query(ObjectType):
#     subscribers = DjangoConnectionField(SubscriberType)
#     subscriber = Field(SubscriberType, id=Argument(ID, required=True))
#     sneakers = DjangoConnectionField(SneakerType)
#     sneaker = Field(SneakerType, id=Argument(ID, required=True))
#
#     def resolve_subscribers(root, info, **kwargs):
#         return Subscriber.objects.all()
#
#     def resolve_subscriber(root, info, **kwargs):
#         return Subscriber.objects.get(id=kwargs.get('id'))
#
#     def resolve_sneakers(root, info, **kwargs):
#         return Sneaker.objects.all()
#
#     def resolve_sneaker(root, info, **kwargs):
#         return Sneaker.objects.get(id=kwargs.get('id'))
#
#
# schema = Schema(query=Query)
