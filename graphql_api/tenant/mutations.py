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
        schema_name = graphene.String(required=True)
        domain_url = graphene.String(required=False)

    def mutate(self, info, tenant_name, paid_until, on_trial, schema_name, domain_url=None):
        client = Client(
            tenant_name=tenant_name,
            paid_until=paid_until,
            on_trial=on_trial,
            schema_name=schema_name,
            domain_url=domain_url
        )
        client.save()
        return CreateClient(client=client)

class UpdateClient(graphene.Mutation):
    client = graphene.Field(ClientType)

    class Arguments:
        id = graphene.Int(required=True)
        tenant_name = graphene.String()
        paid_until = graphene.Date()
        on_trial = graphene.Boolean()
        schema_name = graphene.String()
        domain_url = graphene.String()

    def mutate(self, info, id, tenant_name=None, paid_until=None, on_trial=None, schema_name=None, domain_url=None):
        try:
            client = Client.objects.get(pk=id)
        except Client.DoesNotExist:
            return UpdateClient(client=None)

        if tenant_name:
            client.tenant_name = tenant_name
        if paid_until:
            client.paid_until = paid_until
        if on_trial is not None:
            client.on_trial = on_trial
        if schema_name:
            client.schema_name = schema_name
        if domain_url:
            client.domain_url = domain_url
        client.save()
        return UpdateClient(client=client)

class DeleteClient(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id):
        try:
            client = Client.objects.get(pk=id)
            client.delete()
            return DeleteClient(success=True)
        except Client.DoesNotExist:
            return DeleteClient(success=False)

class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    delete_client = DeleteClient.Field()
