from unittest import TestCase
from unittest.mock import patch

from accounts.services import profileService
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

    @patch('core.core_service.SoleHuntBaseService.create')
    def testCreate(self, mockCreate):
        UseCaseManager(serviceMethod=profileService.create, filters=FILTERS.CREATE_PROFILE).execute()
        mockCreate.assert_called_once()

    @patch('core.core_service.SoleHuntBaseService.update')
    def testUpdate(self, mockUpdate):
        UseCaseManager(serviceMethod=profileService.update, filters=FILTERS.UPDATE_PROFILE).execute()
        mockUpdate.assert_called_once()

    def testDelete(self):
        pass

    def testGet(self):
        pass
