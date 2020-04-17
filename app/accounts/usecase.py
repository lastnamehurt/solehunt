from accounts.services import profileService
from core.usecases import BaseUseCase


class CreateProfileUseCase(BaseUseCase):
    serviceMethod = profileService.createNewProfileInstance


class UpdateProfileUseCase(BaseUseCase):
    serviceMethod = profileService.updateProfile


class GetProfilesUseCase(BaseUseCase):
    serviceMethod = profileService.getAllProfiles


class DeleteProfileUseCase(BaseUseCase):
    serviceMethod = profileService.deleteProfile


class DeactivateRegistrationUseCase(BaseUseCase):
    filters = {'isRegistered': False}
    serviceMethod = profileService.update

