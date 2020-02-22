

class BaseRepo:
    __metaclass__ = None

    repo = __metaclass__

    def __init__(self):
        if not self.repo:
            raise ValueError("Repo Required")

    def getById(self, modelId):
        return self.repo.objects.get(id=modelId)

    def getByFilter(self, **kwargs):
        return self.repo.objects.filter(**kwargs)

    def create(self, **kwargs):
        return self.repo.objects.create(**kwargs)

    def delete(self, modelId):
        return self.repo.objects.get(id=modelId).delete()

    def update(self, modelId, **kwargs):
        return self.repo.objects.filter(id=modelId).update(**kwargs)
