import graphene

from accounts.schema import Query as accountsQuery
from subscribers.schema import Query as subscribersQuery
from blog.schema import Query as blogQuery


# https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/
class Query(
    subscribersQuery,
    accountsQuery,
    blogQuery,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
