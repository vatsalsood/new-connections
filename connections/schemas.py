from marshmallow import fields,validates, ValidationError
from marshmallow_enum import EnumField
from datetime import date
from connections.extensions import ma
from connections.models.connection import Connection, ConnectionType
from connections.models.person import Person


class BaseModelSchema(ma.ModelSchema):
    def __init__(self, strict=True, **kwargs):
        super().__init__(strict=strict, **kwargs)


# date of birth should be less than today's date
# There is not validation for email. Added validation
class PersonSchema(BaseModelSchema):
    email = fields.Email()
    date_of_birth = fields.Date()
    @validates("date_of_birth")
    def validate_date_of_birth(self,value):
        if date.today() < value:
            raise ValidationError("Cannot be in the future.")

    class Meta:
        model = Person
        load_instance = True 



class ConnectionSchema(BaseModelSchema):
    from_person_id = fields.Integer()
    to_person_id = fields.Integer()
    connection_type = EnumField(ConnectionType)

    class Meta:
        model = Connection
        load_instance = True 
