from typing import Dict
from typing import TypeVar

from posts.models import Like


class LikeSchema:
    LIKE_POST = Dict[int, int]
    LIKE_OBJECT = TypeVar('LIKE_OBJECT', bound=Like)
