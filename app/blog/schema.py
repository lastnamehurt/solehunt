import graphene
from graphene_django.types import DjangoObjectType

from blog.services import blogService
from subscribers.schema import SubscriberType


class BlogType(DjangoObjectType):
    class Meta:
        model = blogService.repo.model


class Query:
    all_blogs = graphene.List(BlogType)
    blog = graphene.Field(BlogType,
                          id=graphene.Int(),
                          post_id=graphene.String(),
                          title=graphene.String(),
                          body=graphene.String(),
                          publishedAt=graphene.Time(),
                          url=graphene.String(),
                          )

    def resolve_all_blogs(self, info, **kwargs):
        return blogService.getAllObjects()

    def resolve_blog(self, info, **kwargs):
        blogId = kwargs.get('id', None)
        if blogId is not None:
            return blogService.get(blogId)
