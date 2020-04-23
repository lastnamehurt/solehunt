from accounts.repos.profile_repo import profileRepo
from core.core_service import SoleHuntBaseService


class ProfileService(SoleHuntBaseService):
    repo = profileRepo

    @classmethod
    def getAllProfiles(cls):
        return cls.getAllObjects()

    @classmethod
    def createNewProfileInstance(cls, filters):
        return cls.prepare(filters)

    @classmethod
    def deleteProfile(cls, profileId):
        cls.delete(profileId)

    @classmethod
    def updateProfile(cls, profileId, filters):
        cls.update(profileId, filters)


profileService = ProfileService()
