"""Integration tests for Flask app endpoints."""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test that the /health endpoint returns 200 and correct status."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'


def test_index_endpoint(client):
    """Test that the index endpoint returns 200."""
    response = client.get('/')
    assert response.status_code == 200


def test_add_item_endpoint(client):
    """Test adding an item via POST."""
    response = client.post('/add', data={'item': 'test item'}, follow_redirects=True)
    assert response.status_code == 200
