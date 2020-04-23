from typing import Dict
from typing import List
from typing import TypeVar

from blog.models import BlogPost


class ResponseType:
    POST = Dict[str, str]
    GET_POSTS = Dict[str, List[Dict[str, str]]]
    CREATE = Dict[str, List[Dict[str, str]]]
    PARSED = Dict[str, str]
    BLOG_OBJECT = TypeVar('BLOG_OBJECT', bound=BlogPost)
    BLOG_POSTS = List[BLOG_OBJECT]
