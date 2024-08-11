import graphene
from graphene_django import DjangoObjectType
from tenant.models import Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = "__all__"

class CreateClient(graphene.Mutation):
    client = graphene.Field(ClientType)

    class Arguments:
        tenant_name = graphene.String(required=True)
        paid_until = graphene.Date(required=True)
        on_trial = graphene.Boolean(required=True)

    def mutate(self, info, tenant_name, paid_until, on_trial):
        client = Client(
            tenant_name=tenant_name,
            paid_until=paid_until,
            on_trial=on_trial
        )
        client.save()
        return CreateClient(client=client)

class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
