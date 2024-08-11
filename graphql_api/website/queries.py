import graphene
from graphene_django.types import DjangoObjectType
from website.models import Record

# Type GraphQL pour Record
class RecordType(DjangoObjectType):
    class Meta:
        model = Record
        fields = "__all__"

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