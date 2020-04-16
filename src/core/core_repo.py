

class BaseRepo(object):
    __metaclass__ = None

    model = __metaclass__

    @classmethod
    def query(cls):
        return cls.model.objects

    @classmethod
    def _get(cls, modelId):
        return cls.query().get(id=modelId)

    @classmethod
    def fetchAll(cls):
        return cls.query().all()

    @classmethod
    def count(cls, **kwargs):
        return cls.query().filter(**kwargs).count()

    @classmethod
    def getById(cls, modelId):
        return cls._get(modelId)

    @classmethod
    def getByFilter(cls, **kwargs):
        """
        essentially the same as query()
        """
        return cls.query().filter(**kwargs)

    @classmethod
    def create(cls, filters):
        return cls.query().create(**filters)

    @classmethod
    def prepareModel(cls, **kwargs):
        return cls.model(**kwargs)

    @classmethod
    def exists(cls, **kwargs):
        return cls.query().filter(**kwargs).exists()

    @classmethod
    def deleteById(cls, modelId):
        return cls.query().get(id=modelId).delete()

    @classmethod
    def update(cls, modelId, **kwargs):
        cls.query().filter(id=modelId).update(**kwargs)

    @classmethod
    def createOrUpdate(cls, **kwargs):
        return cls.update(kwargs.get('id'), **kwargs) if cls.exists(id=kwargs.get('id', None)) else cls.create(
            **kwargs)

    @classmethod
    def save(cls, modelId):
        return cls.query().get(id=modelId).save()

# def _query(cls, fields=None):
#     djangoFields = [
#         cls._m
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
