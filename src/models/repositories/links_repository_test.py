import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip("interacao com o banco")
def test_create_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "https://example.com",
        "title": "Example Link",
    }

    links_repository.create_link(link_infos)

@pytest.mark.skip("interacao com o banco")
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links = links_repository.find_links_from_trip(trip_id)
    
    assert isinstance(links, list)
    assert isinstance(links[0], tuple)