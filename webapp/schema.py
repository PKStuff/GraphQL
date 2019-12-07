import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Employee

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee

class Query(ObjectType):
    employee = graphene.Field(EmployeeType, id=graphene.String())
    employees = graphene.List(EmployeeType)

    def resolve_employee(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Employee.objects.get(pk=id)
        
        return None
    
    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all()

schema = graphene.Schema(query=Query)