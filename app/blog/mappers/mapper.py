from blog.mappers.type_mapper import ResponseSchema
from blog.services import blogService


class GhostApiMapper:

    @classmethod
    def toBlogModel(cls, apiResponses: ResponseSchema.GET_POSTS) -> ResponseSchema.BLOG_POSTS:
        postsData = apiResponses['posts']
        newBlogs = [None] * len(postsData)
        blogIndex = 0
        for postData in postsData:
            data = cls.parseBlogPost(postData)
            newBlogs[blogIndex] = blogService.prepare(filters=data)
            blogIndex += 1
        return newBlogs

    @classmethod
    def parseBlogPost(cls, apiResponse: ResponseSchema.POST) -> ResponseSchema.PARSED:
        return {
            'post_id': apiResponse['id'],
            'slug': apiResponse['slug'],
            'title': apiResponse['title'],
            'body': apiResponse['html'],
            'timestamp': apiResponse['published_at'],
            'url': apiResponse['url'],
            'excerpt': apiResponse['excerpt']
        }


ghostApiMapper = GhostApiMapper()
