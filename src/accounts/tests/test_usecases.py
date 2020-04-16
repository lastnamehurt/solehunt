from unittest import TestCase
from unittest.mock import patch

from accounts.usecase import CreateProfileUseCase
from accounts.usecase import DeleteProfileUseCase
from accounts.usecase import GetProfilesUseCase
from accounts.usecase import UpdateProfileUseCase
from core.usecase import UseCaseManager
from utils.helpers import copyAndUpdateDict


class FILTERS:
    CREATE_PROFILE = {
        'first_name': 'sole',
        'last_name': 'hunt',
        'email': 'sole@hunt.com',
        'bio': 'asdfasdfasdfasdf'
    }
    UPDATE_PROFILE = copyAndUpdateDict(CREATE_PROFILE, {'bio': 'testing'})


class ProfileUseCaseTest(TestCase):

    @patch('core.core_service.SoleHuntBaseService.prepare')
    def testCreate(self, mockPrepare):
        UseCaseManager(CreateProfileUseCase, filters=FILTERS.CREATE_PROFILE).execute()
        mockPrepare.assert_called_once()

    @patch('core.core_service.SoleHuntBaseService.update')
    def testUpdate(self, mockUpdate):
        UseCaseManager(UpdateProfileUseCase, filters=FILTERS.UPDATE_PROFILE, modelId=1).execute()
        mockUpdate.assert_called_once()

    @patch('core.core_service.SoleHuntBaseService.delete')
    def testDelete(self, mockDelete):
        UseCaseManager(DeleteProfileUseCase, modelId=1).execute()
        mockDelete.assert_called_once()
        mockDelete.assert_called_once_with(1)

    @patch('core.core_service.SoleHuntBaseService.getAllObjects')
    def testGetProfiles(self, mockGetAllObjects):
        UseCaseManager(GetProfilesUseCase).execute()
        mockGetAllObjects.assert_called_once()