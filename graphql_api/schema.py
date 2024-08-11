import graphene
from graphql_api.website.queries import Query as WebsiteQuery
from graphql_api.website.mutations import Mutation as WebsiteMutation
from graphql_api.tenant.queries import Query as TenantQuery
from graphql_api.tenant.mutations import Mutation as TenantMutation

class Query(WebsiteQuery, TenantQuery, graphene.ObjectType):
    pass

class Mutation(WebsiteMutation, TenantMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)