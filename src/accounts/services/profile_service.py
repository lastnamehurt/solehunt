import logging

from accounts.models import Profile
from accounts.repos.profile_repo import profileRepo


class ProfileService(object):

    repo = profileRepo

    @classmethod
    def get(cls, profileId):
        instance = cls.repo.getById(profileId)
        return instance

    @classmethod
    def getAllProfiles(cls):
        return cls.repo.fetchAll()

    @classmethod
    def createNewProfileInstance(cls, filters):
        instance = cls.repo.prepareModel(**filters)
        return instance

    @classmethod
    def deleteProfile(cls, profileId):
        cls.repo.deleteById(profileId)

    @classmethod
    def updateProfile(cls, profileId, filters):
        cls.repo.update(profileId, **filters)

    @classmethod
    def getOrCreateProfile(cls, filters):
        profileId = filters.get('id', None)
        try:
            instance = cls.repo.getById(profileId)
            return instance
        except Profile.DoesNotExist:
            logging.info('Profile with ID {} does not exist'.format(profileId))
            newInstance = cls.repo.create(**filters)
            return newInstance


profileService = ProfileService()
