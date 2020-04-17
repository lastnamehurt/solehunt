from unittest import TestCase
from unittest.mock import patch

from core.usecase import UseCaseManager
from sneaker_rack.usecase import CreateSneakerRackUseCase
from sneaker_rack.usecase import CreateSneakerUseCase
from sneaker_rack.usecase import DeleteSneakerRackUseCase
from sneaker_rack.usecase import DeleteSneakerUseCase
from sneaker_rack.usecase import GetSneakerRackUseCase
from sneaker_rack.usecase import GetSneakerUseCase
from sneaker_rack.usecase import UpdateSneakerRackUseCase
from sneaker_rack.usecase import UpdateSneakerUseCase
from subscribers.seed import subscriberSeeder
from utils.helpers import copyAndUpdateDict


class FILTERS:
    CREATE_SNEAKER = {
        'brand': 'Nike',
        'color': 'Black',
        'size': '10',
        'Air Max': 'style',
    }
    UPDATE_SNEAKER = copyAndUpdateDict(CREATE_SNEAKER, {'body': 'hunting season!'})
    CREATE_RACK = {'subscriber': subscriberSeeder.seedSubscriber()}

class SneakerUseCaseTest(TestCase):

    @patch('core.core_repo.BaseRepo.create')
    def testCreateSneaker(self, mockCreate):
        UseCaseManager(CreateSneakerUseCase, filters=FILTERS.CREATE_SNEAKER).execute()
        mockCreate.assert_called_once()

    @patch('core.core_repo.BaseRepo.update')
    def testUpdateSneaker(self, mockUpdate):
        UseCaseManager(UpdateSneakerUseCase, filters=FILTERS.UPDATE_SNEAKER, modelId=1).execute()
        mockUpdate.assert_called_once()

    @patch('core.core_repo.BaseRepo.deleteById')
    def testDeleteSneaker(self, mockDelete):
        UseCaseManager(DeleteSneakerUseCase, modelId=1).execute()
        mockDelete.assert_called_once()
        mockDelete.assert_called_once_with(1)

    @patch('core.core_repo.BaseRepo.getById')
    def testGetSneaker(self, mockGetAllObjects):
        UseCaseManager(GetSneakerUseCase, modelId=1).execute()
        mockGetAllObjects.assert_called_once()


class SneakerRackUseCaseTest(TestCase):

    @patch('core.core_repo.BaseRepo.create')
    def testCreateRack(self, mockCreate):
        UseCaseManager(CreateSneakerRackUseCase, filters=FILTERS.CREATE_RACK).execute()
        mockCreate.assert_called_once()

    @patch('core.core_repo.BaseRepo.update')
    def testUpdateRack(self, mockUpdate):
        UseCaseManager(UpdateSneakerRackUseCase, filters=FILTERS.UPDATE_SNEAKER, modelId=1).execute()
        mockUpdate.assert_called_once()

    @patch('core.core_repo.BaseRepo.deleteById')
    def testDeleteRack(self, mockDelete):
        UseCaseManager(DeleteSneakerRackUseCase, modelId=1).execute()
        mockDelete.assert_called_once()
        mockDelete.assert_called_once_with(1)

    @patch('core.core_repo.BaseRepo.getById')
    def testGetRack(self, mockGetAllObjects):
        UseCaseManager(GetSneakerRackUseCase, modelId=1).execute()
        mockGetAllObjects.assert_called_once()
