from django.test import TestCase


# Create your tests here.
class BlogApiServiceTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def testCreatePost(self):
        """
        create blog post model in db
        """
        pass

    def testGetPostById(self):
        pass

    def testGetPostByAuthorName(self):
        pass

    def testGetPostByTitle(self):
        pass

    def testSearchPostsByContent(self):
        pass

    def testDeletePostById(self):
        pass

    def testDeletePostsByIds(self):
        pass

    def testUpdatePostById(self):
        pass

    def testUpdateOrCreatePost(self):
        pass

    def testGetPostsByFilter(self):
        pass
