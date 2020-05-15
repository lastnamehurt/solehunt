import graphene
from graphene_django.types import DjangoObjectType

from core import UseCaseManager as useCaseManager
from posts.models import Like
from posts.models import Post
from posts.usecases import GetLikeUseCase
from posts.usecases import GetLikesUseCase
from posts.usecases import GetPostUseCase
from posts.usecases import GetPostsUseCase


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class LikeType(DjangoObjectType):
    class Meta:
        model = Like


class Query(object):
    all_posts = graphene.List(PostType)
    post = graphene.Field(PostType,
                          id=graphene.Int(),
                          title=graphene.String(),
                          slug=graphene.String(),
                          body=graphene.String(),
                          isActive=graphene.Boolean(),
                          timestamp=graphene.Time(),
                          )

    all_likes = graphene.List(LikeType)
    like = graphene.Field(LikeType,
                          id=graphene.Int(),
                          isActive=graphene.Boolean(),
                          createdAt=graphene.Time(),
                          )

    def resolve_all_posts(self, info, **kwargs):
        return useCaseManager(GetPostsUseCase).execute()

    def resolve_post(self, info, **kwargs):
        postId = kwargs.get('id', None)
        return useCaseManager(GetPostUseCase, modelId=postId).execute() if postId else None

    def resolve_all_likes(self, info, **kwargs):
        return useCaseManager(GetLikesUseCase).execute()

    def resolve_like(self, info, **kwargs):
        likeId = kwargs.get('id', None)
        return useCaseManager(GetLikeUseCase, modelId=likeId).execute() if likeId else None
