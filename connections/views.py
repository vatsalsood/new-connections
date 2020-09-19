from http import HTTPStatus

from flask import Blueprint
from webargs.flaskparser import use_args

from connections.models.person import Person
from connections.models.connection import Connection

from connections.schemas import ConnectionSchema, PersonSchema
import pprint

blueprint = Blueprint('connections', __name__)


@blueprint.route('/people', methods=['GET'])
def get_people():
    people_schema = PersonSchema(many=True)
    people = Person.query.all()
    return people_schema.jsonify(people), HTTPStatus.OK


@blueprint.route('/people', methods=['POST'])
@use_args(PersonSchema(), locations=('json',))
def create_person(person):
    person.save()
    return PersonSchema().jsonify(person), HTTPStatus.CREATED

@blueprint.route('/connections', methods=['GET'])
def get_connection():
    connection_schema = ConnectionSchema(many=True)
    connection = Connection.query.join(Person,Person.id == Connection.from_person_id).all()
    pprint.pprint(connection[0])
    return connection_schema.jsonify(connection), HTTPStatus.OK
    # return json.dumps(connection), HTTPStatus.OK


@blueprint.route('/connections', methods=['POST'])
@use_args(ConnectionSchema(), locations=('json',))
def create_connection(connection):
    connection.save()
    return ConnectionSchema().jsonify(connection), HTTPStatus.CREATED

    
@blueprint.route('/connections/<connection_id>', methods=['PATCH'])
@use_args(ConnectionSchema(), locations=('json',))
def patch_connection(connection,connection_id):
    Connection.update().filter(Connection.id == connection_id)
    return ConnectionSchema().jsonify(connection), HTTPStatus.CREATED

