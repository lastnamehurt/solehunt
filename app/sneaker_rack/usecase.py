from core.usecases import BaseUseCase
from sneaker_rack.services.sneaker_service import rackService
from sneaker_rack.services.sneaker_service import sneakerService


class CreateSneakerUseCase(BaseUseCase):
    serviceMethod = sneakerService.create


class UpdateSneakerUseCase(BaseUseCase):
    serviceMethod = sneakerService.update


class DeleteSneakerUseCase(BaseUseCase):
    serviceMethod = sneakerService.delete


class GetSneakerUseCase(BaseUseCase):
    serviceMethod = sneakerService.get


# SneakerRack UseCases
class CreateSneakerRackUseCase(BaseUseCase):
    serviceMethod = rackService.create


class UpdateSneakerRackUseCase(BaseUseCase):
    serviceMethod = rackService.update


class DeleteSneakerRackUseCase(BaseUseCase):
    serviceMethod = rackService.delete


class GetSneakerRackUseCase(BaseUseCase):
    serviceMethod = rackService.get
