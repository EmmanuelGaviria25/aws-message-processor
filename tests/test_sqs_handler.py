from src.aws.sqs_handler import receive_messages, delete_message
from unittest.mock import patch

@patch("boto3.client")
def test_receive_messages(mock_boto_client):
    mock_boto_client.return_value.receive_message.return_value = {
        "Messages": [{"Body": "Test message", "ReceiptHandle": "12345"}]
    }
    messages = receive_messages("dummy-url")
    assert len(messages) == 1

@patch("boto3.client")
def test_delete_message(mock_boto_client):
    delete_message("dummy-url", "12345")
    mock_boto_client.return_value.delete_message.assert_called_once()
