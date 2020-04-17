from blog.mappers.type_mapper import ResponseType
from blog.services import blogService


class GhostApiMapper:

    @classmethod
    def toBlogModel(cls, apiResponses: ResponseType.GET_POSTS) -> ResponseType.BLOG_POSTS:
        newBlogs = []
        postsData = apiResponses['posts']
        for postData in postsData:
            data = cls.parseBlogPost(postData)
            newBlogs.append(blogService.prepare(filters=data))
        return newBlogs

    @classmethod
    def parseBlogPost(cls, apiResponse: ResponseType.POST) -> ResponseType.PARSED:
        return {
            'post_id': apiResponse['id'],
            # 'author': response['author'],
            'slug': apiResponse['slug'],
            'title': apiResponse['title'],
            'body': apiResponse['html'],
            'timestamp': apiResponse['published_at'],
            'url': apiResponse['url'],
            'excerpt': apiResponse['excerpt']
        }


ghostApiMapper = GhostApiMapper()
