from unittest import TestCase
from unittest.mock import patch


from core.usecases import UseCaseManager
from posts.usecase import CreatePostUseCase
from posts.usecase import DeletePostUseCase
from posts.usecase import GetPostUseCase
from posts.usecase import UpdatePostUseCase
from utils.helpers import copyAndUpdateDict


class FILTERS:
    CREATE_POST = {
        'post_id': '1',
        'slug': 'test',
        'title': 'hunting season',
        'body': 'time to hunt',
    }
    UPDATE_POST = copyAndUpdateDict(CREATE_POST, {'body': 'hunting season!'})


class PostUseCaseTest(TestCase):

    @patch('core.core_repo.BaseRepo.create')
    def testCreatePost(self, mockCreate):
        UseCaseManager(CreatePostUseCase, filters=FILTERS.CREATE_POST).execute()
        mockCreate.assert_called_once()

    @patch('core.core_repo.BaseRepo.update')
    def testUpdatePost(self, mockUpdate):
        UseCaseManager(UpdatePostUseCase, filters=FILTERS.UPDATE_POST, modelId=1).execute()
        mockUpdate.assert_called_once()

    @patch('core.core_repo.BaseRepo.deleteById')
    def testDeletePost(self, mockDelete):
        UseCaseManager(DeletePostUseCase, modelId=1).execute()
        mockDelete.assert_called_once()
        mockDelete.assert_called_once_with(1)

    @patch('core.core_repo.BaseRepo.getById')
    def testGetPost(self, mockGetAllObjects):
        UseCaseManager(GetPostUseCase, modelId=1).execute()
        mockGetAllObjects.assert_called_once()