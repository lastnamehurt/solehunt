def reloadObject(obj):
    """
    reloads Django object
    """
    obj.refresh_from_db()
    return obj


def copyAndUpdateDict(filterDict, filters):
    res = filterDict.copy()
    res.update(**filters)
    return res


def extractPostAndLikedByIdFromFilters(filters):
    if 'postId' in filters:
        filters['post_id'] = filters['postId']
        del filters['postId']

    if 'likedById' in filters:
        filters['likedBy_id'] = filters['likedById']
        del filters['likedById']

    postId = filters.get('postId', None) or filters.get('post_id', None)
    likedById = filters.get('likedBy_id', None) or filters.get('likedById', None)
    return postId, likedById


class LikeFilters:
    LIKE_POST = {
        'post_id': 1,
        'likedBy_id': 1,
    }


class FILTERS:
    CREATE_POST = {
        'slug': 'test',
        'title': 'hunting season',
        'body': 'time to hunt',
    }
