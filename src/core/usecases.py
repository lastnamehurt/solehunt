class BaseUseCase:
    serviceMethod = None
    modelId = None
    filters = {}

    @classmethod
    def execute(cls):
        if cls.modelId and cls.filters:
            return cls.serviceMethod(cls.modelId, filters=cls.filters)
        if cls.modelId and not cls.filters:
            return cls.serviceMethod(cls.modelId)

        if cls.filters and not cls.modelId:
            return cls.serviceMethod(filters=cls.filters)
        else:
            return cls.serviceMethod()


class UseCaseManager:

    def __init__(self, useCase, filters=None, modelId=None):
        if filters is None:
            filters = {}
        self.serviceMethod = useCase.serviceMethod
        self.filters = filters
        self.modelId = modelId

    def execute(self):
        BaseUseCase.serviceMethod = self.serviceMethod
        BaseUseCase.filters = self.filters
        BaseUseCase.modelId = self.modelId
        return BaseUseCase.execute()
