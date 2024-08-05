from graphene_django.types import DjangoObjectType
from .models import Record

class RecordType(DjangoObjectType):
    class Meta:
        model = Record
