

class BaseRepo:
    __metaclass__ = None

    repo = __metaclass__

    def __init__(self):
        if not self.repo:
            raise ValueError("Repo Required")

    def query(self):
        return self.repo.objects

    def _get(self, modelId):
        self.query().get(id=modelId)

    def fetchAll(self):
        return self.query().all()

    def count(self, **kwargs):
        return self.query().filter(**kwargs).count()

    def getById(self, modelId: int) -> object:
        return self._get(modelId)

    def getByFilter(self, **kwargs):
        """
        essentially the same as query()
        """
        return self.query().filter(**kwargs)

    def create(self, filters):
        return self.query().create(**filters)

    def prepareModel(self, **kwargs):
        return self.repo(**kwargs)

    def exists(self, **kwargs):
        return self.query().filter(**kwargs).exists()

    def deleteById(self, modelId):
        return self.query().get(id=modelId).delete()

    def update(self, modelId, **kwargs):
        return self.query().filter(id=modelId).update(**kwargs)

    def createOrUpdate(self, **kwargs):
        return self.update(kwargs.get('id'), **kwargs) if self.exists(id=kwargs.get('id', None)) else self.create(
            **kwargs)

# def _query(self, fields=None):
#     djangoFields = [
#         self._m
#     ]

# class ModelRepoMetaClass(type):
#     def __new__(cls, name, bases, attrs, *args, **kwargs):
#         super_new = super(ModelRepoMetaClass, cls).__new__
#
#         parents = [b for b in bases if isinstance(b, ModelRepoMetaClass)]
#         if not parents:
#             return super_new(cls, name, bases, attrs, *args, **kwargs)
#
#         meta = attrs.pop('Meta', None)
#         new_class = super_new(cls, name, bases, attrs, *args, **kwargs)
#         new_class._meta = meta
#
#         return new_class
