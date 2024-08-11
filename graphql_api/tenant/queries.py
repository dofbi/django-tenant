import graphene
from graphene_django import DjangoObjectType
from tenant.models import Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = "__all__"

class Query(graphene.ObjectType):
    all_clients = graphene.List(ClientType)

    def resolve_all_clients(root, info):
        return Client.objects.all()
