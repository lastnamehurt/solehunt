from accounts.services import profileService
from core.usecase import BaseUseCase


class CreateProfileUseCase(BaseUseCase):
    serviceMethod = profileService.create


class UpdateProfileUseCase(BaseUseCase):
    serviceMethod = profileService.updateProfile


class GetProfileUseCase(BaseUseCase):
    serviceMethod = profileService.get


class DeleteProfileUseCase(BaseUseCase):
    serviceMethod = profileService.delete


class DeactivateRegistrationUseCase(BaseUseCase):
    filters = {'isRegistered': False}
    serviceMethod = profileService.update

