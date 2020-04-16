from unittest import TestCase
from unittest.mock import patch

from blog.usecase import CreateBlogUseCase
from blog.usecase import DeleteBlogUseCase
from blog.usecase import GetBlogUseCase
from blog.usecase import UpdateBlogUseCase
from core.usecase import UseCaseManager
from utils.helpers import copyAndUpdateDict


class FILTERS:
    CREATE_BLOG = {
        'post_id': '1',
        'slug': 'test',
        'title': 'hunting season',
        'body': 'time to hunt',
    }
    UPDATE_BLOG = copyAndUpdateDict(CREATE_BLOG, {'body': 'hunting season!'})


class ProfileUseCaseTest(TestCase):

    @patch('core.core_repo.BaseRepo.create')
    def testCreateBlog(self, mockCreate):
        UseCaseManager(CreateBlogUseCase, filters=FILTERS.CREATE_BLOG).execute()
        mockCreate.assert_called_once()

    @patch('core.core_repo.BaseRepo.update')
    def testUpdateBlog(self, mockUpdate):
        UseCaseManager(UpdateBlogUseCase, filters=FILTERS.UPDATE_BLOG, modelId=1).execute()
        mockUpdate.assert_called_once()

    @patch('core.core_repo.BaseRepo.deleteById')
    def testDeleteBlog(self, mockDelete):
        UseCaseManager(DeleteBlogUseCase, modelId=1).execute()
        mockDelete.assert_called_once()
        mockDelete.assert_called_once_with(1)

    @patch('core.core_repo.BaseRepo.getById')
    def testGetProfiles(self, mockGetAllObjects):
        UseCaseManager(GetBlogUseCase, modelId=1).execute()
        mockGetAllObjects.assert_called_once()