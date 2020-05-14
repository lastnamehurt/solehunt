from datetime import datetime, timezone

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

    def seedBlog(self, subscriber=None):
        BLOG_DICT['subscriber'] = subscriber
        blog = blogService.prepare(filters=BLOG_DICT)
        blog.save()
        return blog


blogSeeder = BlogSeeder()
