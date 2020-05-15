import graphene
from graphene_django.types import DjangoObjectType

from blog.models import BlogPost
from blog.usecase import GetBlogUseCase
from blog.usecase import GetBlogsUseCase
from core import UseCaseManager as useCaseManager


class BlogType(DjangoObjectType):
    class Meta:
        model = BlogPost


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
        return useCaseManager(GetBlogsUseCase).execute()

    def resolve_blog(self, info, **kwargs):
        blogId = kwargs.get('id', None)
        return useCaseManager(GetBlogUseCase, modelId=blogId).execute() if blogId else None
