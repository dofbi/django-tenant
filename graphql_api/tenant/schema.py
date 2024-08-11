import graphene
from .queries import Query as TenantQuery
from .mutations import Mutation as TenantMutation

class Query(TenantQuery, graphene.ObjectType):
    pass

class Mutation(TenantMutation, graphene.ObjectType):
    pass
