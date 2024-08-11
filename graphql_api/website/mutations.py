import graphene
from graphene_django.types import DjangoObjectType
from website.models import Record

class RecordType(DjangoObjectType):
    class Meta:
        model = Record
        fields = "__all__"

# Mutation pour créer un enregistrement
class CreateRecord(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)
        address = graphene.String(required=True)
        city = graphene.String(required=True)
        state = graphene.String(required=True)
        zipcode = graphene.String(required=True)

    record = graphene.Field(lambda: RecordType)

    def mutate(self, info, first_name, last_name, email, phone, address, city, state, zipcode):
        record = Record(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            adress=address,
            city=city,
            state=state,
            zipcode=zipcode
        )
        record.save()
        return CreateRecord(record=record)

# Mutation pour mettre à jour un enregistrement
class UpdateRecord(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        address = graphene.String()
        city = graphene.String()
        state = graphene.String()
        zipcode = graphene.String()

    record = graphene.Field(lambda: RecordType)

    def mutate(self, info, id, first_name=None, last_name=None, email=None, phone=None, address=None, city=None, state=None, zipcode=None):
        record = Record.objects.get(pk=id)
        if first_name:
            record.first_name = first_name
        if last_name:
            record.last_name = last_name
        if email:
            record.email = email
        if phone:
            record.phone = phone
        if address:
            record.adress = address
        if city:
            record.city = city
        if state:
            record.state = state
        if zipcode:
            record.zipcode = zipcode
        record.save()
        return UpdateRecord(record=record)

# Mutation pour supprimer un enregistrement
class DeleteRecord(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id):
        record = Record.objects.get(pk=id)
        record.delete()
        return DeleteRecord(success=True)

class Mutation(graphene.ObjectType):
    create_record = CreateRecord.Field()
    update_record = UpdateRecord.Field()
    delete_record = DeleteRecord.Field()