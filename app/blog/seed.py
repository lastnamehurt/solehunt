from datetime import datetime

from blog.services.blog_service import blogService

BLOG_DICT = {
    'post_id': '1',
    'slug': 'hey yall',
    'title': 'what',
    'body': 'ok',
    'context': 'yeah',
    'excerpt': 'because',
    'timestamp': datetime.now()
}


class BlogSeeder(object):

    def seedBlog(self, ):
        blog = blogService.prepare(filters=BLOG_DICT)
        blog.save()
        return blog


blogSeeder = BlogSeeder()
