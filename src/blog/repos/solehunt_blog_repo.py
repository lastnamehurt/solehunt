from core.base_repo import BaseRepo
from blog.models import BlogPost


class SBlogRepo(BaseRepo):

    repo = BlogPost


blogRepo = SBlogRepo()
