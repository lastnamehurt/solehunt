from core.core_service import SoleHuntBaseService
from blog.repos.solehunt_blog_repo import blogRepo


class BlogService(SoleHuntBaseService):

    repo = blogRepo.repo

    @classmethod
    def getPostById(cls, postId):
        return blogRepo.getById(postId)

    @classmethod
    def getPosts(cls):
        return blogRepo.fetchAll()

    @classmethod
    def getPostByAuthorName(cls, authorName):
        return blogRepo.query().get(alias=authorName)

    @classmethod
    def getPostByTitle(cls, title):
        return blogRepo.query().get(title=title)

    @classmethod
    def searchPostContent(cls, searchContent):
        return blogRepo.query().filter(body__icontains=searchContent)

    @classmethod
    def deletePostById(cls, postId):
        blogRepo.deleteById(postId)

    @classmethod
    def deletePostsById(cls, postIds):
        for postId in postIds:
            blogRepo.deleteById(postId)

    @classmethod
    def updatePostById(cls, postId, **kwargs):
        return blogRepo.update(postId, **kwargs)

    @classmethod
    def updateOrCreatePost(cls, **kwargs):
        return blogRepo.createOrUpdate(**kwargs)

    @classmethod
    def createPost(cls, **kwargs):
        return blogRepo.create(**kwargs)

    @classmethod
    def getPostsByFilter(cls, **kwargs):
        return blogRepo.query().filter(**kwargs)

    @classmethod
    def prepare(cls, filters):
        return blogRepo.prepareModel(**filters)


blogService = BlogService()
