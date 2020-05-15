import graphene
from graphene_django.types import DjangoObjectType

from accounts.models import Profile
from accounts.usecase import GetProfileByIdUseCase
from accounts.usecase import GetProfilesUseCase
from core import UseCaseManager


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query:
    all_profiles = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, id=graphene.Int(), first_name=graphene.String(), last_name=graphene.String())

    def resolve_all_profiles(self, info, **kwargs):
        return UseCaseManager(GetProfilesUseCase).execute()

    def resolve_profile(self, info, **kwargs):
        profileId = kwargs.get('id', None)
        if profileId is not None:
            return UseCaseManager(GetProfileByIdUseCase, modelId=profileId).execute()
