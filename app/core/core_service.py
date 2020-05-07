import logging


class SoleHuntBaseService(object):

    repo = None

    @classmethod
    def get(cls, modelId):
        return cls.repo.getById(modelId=modelId)

    @classmethod
    def getAllObjects(cls):
        return cls.repo.fetchAll()

    @classmethod
    def create(cls, filters):
        return cls.repo.create(filters)

    @classmethod
    def getByFilters(cls, filters):
        return cls.repo.query().filter(**filters)

    # noinspection PyBroadException
    @classmethod
    def getOrCreate(cls, filters):
        profileId = filters.get('id', None)
        try:
            instance = cls.repo.getById(profileId)
            return instance
        except cls.repo.model.DoesNotExist:
            logging.info('Model with ID {} does not exist. Creating one'.format(profileId))
            newInstance = cls.repo.create(**filters)
            return newInstance

    @classmethod
    def prepare(cls, filters):
        instance = cls.repo.prepareModel(filters)
        return instance

    @classmethod
    def update(cls, modelId, filters):
        cls.repo.update(modelId, filters)

    @classmethod
    def delete(cls, modelId):
        cls.repo.deleteById(modelId)

    @classmethod
    def updateOrCreate(cls):
        pass