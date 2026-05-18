import pytest
from run import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    # /tasks unvanina muraciet edib cavabi yoxlayir
    rv = client.get('/tasks')
    assert rv.status_code == 200
    assert b'Git ve GitHub oyren' in rv.data
