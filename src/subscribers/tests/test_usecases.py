from unittest import TestCase
from unittest.mock import patch

from core.usecases import UseCaseManager
from subscribers.usecase import ActivateSubscriptionUseCase
from subscribers.usecase import CreateSubscriberUseCase
from subscribers.usecase import DeleteSubscriberUseCase
from subscribers.usecase import GetSubscriberUseCase
from subscribers.usecase import UpdateSubscriberUseCase
from utils.helpers import copyAndUpdateDict


class FILTERS:
    CREATE_SUBSCRIBER = {
        'alias': 'Admin',
        'isActive': 'False',
    }
    UPDATE_SUBSCRIBER = copyAndUpdateDict(CREATE_SUBSCRIBER, {'isActive': True})


class SubscriberUseCaseTest(TestCase):

    @patch('core.core_repo.BaseRepo.create')
    def testCreateSubscriber(self, mockCreate):
        UseCaseManager(CreateSubscriberUseCase, filters=FILTERS.CREATE_SUBSCRIBER).execute()
        mockCreate.assert_called_once()

    @patch('core.core_repo.BaseRepo.update')
    def testUpdateSubscriber(self, mockUpdate):
        UseCaseManager(UpdateSubscriberUseCase, filters=FILTERS.UPDATE_SUBSCRIBER, modelId=1).execute()
        mockUpdate.assert_called_once()

    @patch('core.core_repo.BaseRepo.deleteById')
    def testDeleteSubscriber(self, mockDelete):
        UseCaseManager(DeleteSubscriberUseCase, modelId=1).execute()
        mockDelete.assert_called_once()
        mockDelete.assert_called_once_with(1)

    @patch('core.core_repo.BaseRepo.getById')
    def testGetSubscriber(self, mockGetAllObjects):
        UseCaseManager(GetSubscriberUseCase, modelId=1).execute()
        mockGetAllObjects.assert_called_once()

    @patch('django.db.models.base.Model.save')
    def testActivateSubscription(self, mockSave):
        UseCaseManager(ActivateSubscriptionUseCase, modelId=1).execute()
        mockSave.assert_called_once()