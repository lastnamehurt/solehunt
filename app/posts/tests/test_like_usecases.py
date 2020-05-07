from unittest import TestCase
from unittest.mock import patch

from core.usecases import UseCaseManager
from posts.seed import likeSeeder
from posts.seed import postSeeder
from posts.usecases.like_usecase import LikeCountUseCase
from posts.usecases.like_usecase import LikePostUseCase
from posts.usecases.like_usecase import UnlikePostUseCase
from subscribers.seed import subscriberSeeder
from utils.helpers import LikeFilters


class LikePostUseCaseTest(TestCase):

    def setUp(self):
        self.usecase = UseCaseManager
        self.subscriber = subscriberSeeder.seedSubscriber()
        self.post = postSeeder.seedPost()
        self.like = likeSeeder.seedLike()

    @patch('posts.services.like_service.LikeService.isLiked')
    @patch('core.core_repo.BaseRepo.create')
    @patch('core.core_service.SoleHuntBaseService.getByFilters', return_value=False)
    def testLikePost(self, mockGetByFilters, mockCreate, mockIsLiked):
        self.usecase(LikePostUseCase, filters={'post_id': self.post.id, 'likedBy_id': self.subscriber.id}).execute()
        mockGetByFilters.assert_called_once()
        mockCreate.assert_called_once_with({'post_id': self.post.id, 'likedBy_id': self.subscriber.id})
        mockIsLiked.assert_called_once()

    @patch('posts.services.like_service.LikeService.isLiked')
    @patch('core.core_service.SoleHuntBaseService.getByFilters')
    def testCanOnlyLikePostOnce(self, mockGetByFilters, mockIsLiked):
        self.usecase(LikePostUseCase, filters={'post_id': self.post.id, 'likedBy_id': self.subscriber.id}).execute()
        mockGetByFilters.assert_called_once_with(LikeFilters.LIKE_POST)
        mockIsLiked.assert_called_once()

    @patch('posts.services.like_service.LikeService.isLiked', return_value=True)
    @patch('core.core_service.SoleHuntBaseService.get')
    def testUnlikePost(self, mockQuery, mockCheck):
        self.usecase(UnlikePostUseCase, modelId=self.like.id).execute()
        mockQuery.assert_called_once_with(1)
        self.assertTrue(mockCheck.called)

    @patch('django.db.models.query.QuerySet.count', return_value=4)
    def testGetLikeCount(self, mockCount):
        self.usecase(LikeCountUseCase, modelId=1).execute()
        self.assertTrue(mockCount.called)
        self.assertEqual(4, mockCount.return_value)
