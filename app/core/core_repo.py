from utils.helpers import reloadObject


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
    def count(cls, filters):
        return cls.query().filter(**filters).count()

    @classmethod
    def getById(cls, modelId):
        return cls._get(modelId)

    @classmethod
    def getByFilter(cls, filters):
        """
        essentially the same as query()
        """
        return cls.query().filter(**filters)

    @classmethod
    def create(cls, filters):
        return cls.query().create(**filters)

    @classmethod
    def prepareModel(cls, filters):
        return cls.model(**filters)

    @classmethod
    def exists(cls, filters):
        return cls.query().filter(**filters).exists()

    @classmethod
    def deleteById(cls, modelId):
        return cls.query().get(id=modelId).delete()

    @classmethod
    def update(cls, modelId, filters):
        cls.query().filter(id=modelId).update(**filters)

    @classmethod
    def createOrUpdate(cls, filters):
        return cls.update(filters.get('id'), **filters) if cls.exists(id=filters.get('id', None)) else cls.create(
            **filters)

    @classmethod
    def save(cls, modelId):
        obj = cls.query().get(id=modelId)
        obj.save()
        return reloadObject(obj)


# class ModelRepoMetaClass(type):
#     def __new__(cls, name, bases, attrs, *args, **filters):
#         super_new = super(ModelRepoMetaClass, cls).__new__
#
#         parents = [b for b in bases if isinstance(b, ModelRepoMetaClass)]
#         if not parents:
#             return super_new(cls, name, bases, attrs, *args, **filters)
#
#         meta = attrs.pop('Meta', None)
#         new_class = super_new(cls, name, bases, attrs, *args, **filters)
#         new_class._meta = meta
#
#         return new_class
