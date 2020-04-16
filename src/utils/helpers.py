

def reloadObject(obj):
    """
    reloads Django object
    """
    obj.refresh_from_db()
    return obj