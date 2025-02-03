from src.services.downloader_service import download_urls_concurrently
from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
async def test_download_urls_concurrently(mock_get):
    mock_response = MagicMock()
    mock_response.status = 200
    mock_response.text.return_value = "Success"
    mock_get.return_value.__aenter__.return_value = mock_response

    urls = ["http://example.com/file1", "http://example.com/file2"]
    results = await download_urls_concurrently(urls)
    assert results == ["Success", "Success"]
