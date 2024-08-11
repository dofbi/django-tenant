import graphene
from .queries import Query as WebsiteQuery
from .mutations import Mutation as WebsiteMutation

class Query(WebsiteQuery, graphene.ObjectType):
    pass

class Mutation(WebsiteMutation, graphene.ObjectType):
    pass
