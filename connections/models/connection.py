import enum

from connections.database import CreatedUpdatedMixin, CRUDMixin, db, Model


class ConnectionType(enum.Enum):
    mother = 'mother'
    father = 'father'
    son = 'son'
    daughter = 'daughter'
    husband = 'husband'
    wife = 'wife'
    brother = 'brother'
    sister = 'sister'
    friend = 'friend'
    coworker = 'coworker'

# Attempted doing join but not retrieving correct
class Connection(Model, CRUDMixin, CreatedUpdatedMixin):
    id = db.Column(db.Integer, primary_key=True)
    from_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    to_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    connection_type = db.Column(db.Enum(ConnectionType), nullable=False)
    from_person =  db.relationship("Person", primaryjoin="Connection.from_person_id == Person.id")
    to_person =  db.relationship("Person", primaryjoin="Connection.to_person_id == Person.id")
