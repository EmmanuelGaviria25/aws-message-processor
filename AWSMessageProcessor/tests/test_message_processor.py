from src.services.message_processor import process_sqs_messages
from unittest.mock import patch

@patch("src.services.message_processor.receive_messages")
@patch("src.services.message_processor.insert_to_mongo")
@patch("src.services.message_processor.upload_to_s3")
@patch("src.services.message_processor.delete_message")
def test_process_sqs_messages(mock_delete, mock_upload, mock_insert, mock_receive):
    mock_receive.return_value = [{"Body": '{"id": 1, "name": "Test", "save_to_s3": true}', "ReceiptHandle": "12345"}]
    process_sqs_messages()
    mock_insert.assert_called_once()
    mock_upload.assert_called_once()
    mock_delete.assert_called_once()
