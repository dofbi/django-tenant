import graphene
from graphene_django.types import DjangoObjectType
from .models import Record
from .mutations import CreateRecord, UpdateRecord, DeleteRecord

# Type GraphQL pour Record
class RecordType(DjangoObjectType):
    class Meta:
        model = Record

# Queries pour obtenir les enregistrements
class Query(graphene.ObjectType):
    all_records = graphene.List(RecordType, description="Récupère tous les enregistrements")
    record = graphene.Field(RecordType, id=graphene.Int(), description="Récupère un enregistrement par ID")

    def resolve_all_records(self, info, **kwargs):
        return Record.objects.all()

    def resolve_record(self, info, id):
        try:
            return Record.objects.get(id=id)
        except Record.DoesNotExist:
            return None

# Schéma principal
class Mutation(graphene.ObjectType):
    create_record = CreateRecord.Field(description="Crée un nouvel enregistrement")
    update_record = UpdateRecord.Field(description="Met à jour un enregistrement existant")
    delete_record = DeleteRecord.Field(description="Supprime un enregistrement existant")

schema = graphene.Schema(query=Query, mutation=Mutation)
