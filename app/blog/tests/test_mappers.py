from unittest.mock import patch

from django.test import TestCase

from blog.mappers.mapper import ghostApiMapper
from blog.models import BlogPost
from blog.tests.responses import getPostByIdResponse
from blog.tests.responses import parsedResponse


class GhostApiMapperTest(TestCase):

    @patch('blog.mappers.mapper.GhostApiMapper.parseBlogPost')
    def testToBlogModelCreatesBlogObject(self, mockParsedResponse):
        mockParsedResponse.return_value = parsedResponse
        data = ghostApiMapper.toBlogModel(getPostByIdResponse)
        blogObj = data[0]

        self.assertEqual(1, len(data))
        self.assertIsInstance(data[0], BlogPost)
        self.assertEqual(blogObj.post_id, parsedResponse['post_id'])
        self.assertEqual(blogObj.slug, parsedResponse['slug'])
        self.assertEqual(blogObj.title, parsedResponse['title'])
        self.assertEqual(blogObj.body, parsedResponse['body'])
        self.assertEqual(blogObj.timestamp, parsedResponse['timestamp'])
        self.assertEqual(blogObj.url, parsedResponse['url'])
        self.assertEqual(blogObj.excerpt, parsedResponse['excerpt'])

    def testParsePostFromApi(self):
        post = getPostByIdResponse['posts'][0]
        res = ghostApiMapper.parseBlogPost(post)

        self.maxDiff = None
        self.assertEqual(res['post_id'], post['id'])
        self.assertEqual(res['slug'], post['slug'])
        self.assertEqual(res['title'], post['title'])
