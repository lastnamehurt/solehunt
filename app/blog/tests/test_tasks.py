from unittest.mock import patch

from django.test import TestCase

from blog import tasks as blogTasks
from blog.seed import blogSeeder


class BlogTasksTest(TestCase):

    def setUp(self):
        self.blog = blogSeeder.seedBlog()

    @patch('blog.services.ghost_service.GhostAPIWrapper.getAllPosts')
    @patch('blog.services.blog_service.BlogService.getPosts')
    def testGetOrCreateBlogTask(self, mockGetBlogPosts, mockGetAllPostsFromApi):
        blogs = blogTasks.getOrCreateBlogs()
        self.assertTrue(mockGetAllPostsFromApi.called)
        self.assertTrue(mockGetBlogPosts.called)
        self.assertGreater(len(blogs), 0)
