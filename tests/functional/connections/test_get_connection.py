# Write the unit test case for creating connections

from datetime import date
from http import HTTPStatus

import pytest
from tests.factories import PersonFactory

from connections.models.connection import Connection
from tests.factories import ConnectionFactory

# @pytest.mark.xfail
def test_can_get_connection(db, testapp):
    ConnectionFactory.create_batch(1)
    db.session.commit()
    res = testapp.get('/connections')
    assert res.status_code == HTTPStatus.OK
    # assert len(res.json) == 10
 
