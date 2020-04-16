from core.core_repo import BaseRepo
from blog.models import BlogPost


class SBlogRepo(BaseRepo):

    model = BlogPost


blogRepo = SBlogRepo()
