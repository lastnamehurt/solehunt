from blog.models import BlogPost
from core.core_repo import BaseRepo


class SBlogRepo(BaseRepo):
    model = BlogPost


blogRepo = SBlogRepo()
