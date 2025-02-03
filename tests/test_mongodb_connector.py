from src.database.mongodb_connector import insert_to_mongo, fetch_all_documents
from unittest.mock import patch

@patch("src.database.mongodb_connector.collection")
def test_insert_to_mongo(mock_collection):
    mock_collection.insert_one.return_value.inserted_id = "12345"
    result = insert_to_mongo({"id": 1, "name": "Test", "value": 100.0})
    assert result == "12345"

@patch("src.database.mongodb_connector.collection")
def test_fetch_all_documents(mock_collection):
    mock_collection.find.return_value = [{"id": 1, "name": "Test"}]
    documents = fetch_all_documents()
    assert len(documents) == 1
