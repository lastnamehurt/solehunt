import graphene
from graphene_django.types import DjangoObjectType

from accounts.services import profileService


class ProfileType(DjangoObjectType):
    class Meta:
        model = profileService.repo.model


class Query:
    all_profiles = graphene.List(ProfileType)
    profile = graphene.Field(ProfileType, id=graphene.Int(), first_name=graphene.String(), last_name=graphene.String())

    def resolve_all_profiles(self, info, **kwargs):
        return profileService.getAllObjects()

    def resolve_profile(self, info, **kwargs):
        profileId = kwargs.get('id', None)
        if profileId is not None:
            return profileService.get(profileId)
