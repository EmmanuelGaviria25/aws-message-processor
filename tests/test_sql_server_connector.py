from src.database.sql_server_connector import get_sql_connection, insert_into_sql_server
from unittest.mock import patch, MagicMock

@patch("pyodbc.connect")
def test_get_sql_connection(mock_connect):
    mock_connect.return_value = MagicMock()
    conn = get_sql_connection()
    assert conn is not None

@patch("src.database.sql_server_connector.get_sql_connection")
def test_insert_into_sql_server(mock_get_conn):
    mock_cursor = MagicMock()
    mock_get_conn.return_value.cursor.return_value = mock_cursor
    data = {"id": 1, "name": "Test", "value": 100.0, "timestamp": "2025-02-01 12:00:00"}
    insert_into_sql_server("messages", data)
    mock_cursor.execute.assert_called_once()
