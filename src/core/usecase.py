class BaseUseCase:
    serviceMethod = None
    modelId = None
    filters = {}

    @classmethod
    def execute(cls):
        if cls.modelId and not cls.filters:
            return cls.serviceMethod(cls.modelId)

        if cls.filters and not cls.modelId:
            return cls.serviceMethod(filters=cls.filters)
        else:
            return cls.serviceMethod()


class UseCaseManager:

    def __init__(self, serviceMethod=None, filters=None, modelId=None):
        self.serviceMethod = serviceMethod
        self.filters = filters
        self.modelId = modelId

    def execute(self):
        BaseUseCase.serviceMethod = self.serviceMethod
        BaseUseCase.filters = self.filters
        BaseUseCase.modelId = self.modelId
        return BaseUseCase.execute()