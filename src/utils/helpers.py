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
