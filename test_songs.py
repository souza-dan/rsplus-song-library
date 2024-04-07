import unittest
import os
import json
from unittest.mock import patch, MagicMock
from songs import fetch_songs


class TestFetchSongs(unittest.TestCase):
    def setUp(self):
        # Create a test directory for requests
        self.cache_directory = "test_requests"
        os.makedirs(self.cache_directory, exist_ok=True)

    def tearDown(self):
        # Clean up the test directory for requests
        for filename in os.listdir(self.cache_directory):
            file_path = os.path.join(self.cache_directory, filename)
            os.remove(file_path)
        os.rmdir(self.cache_directory)

    @patch('songs.requests.get')
    def test_fetch_songs_cached(self, mock_get):
        # Prepare mocked response data
        response_data = {'data': [{'songId': 1, 'songName': 'Song 1'}, {'songId': 2, 'songName': 'Song 2'}]}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = response_data
        mock_get.return_value = mock_response

        # Mock the cache file existence
        cache_filename = os.path.join("test_requests", "genre_Rock_page_1_page_size_10.json")
        with open(cache_filename, 'w') as cache_file:
            json.dump(response_data['data'], cache_file)

        # Call the fetch_songs method
        songs = fetch_songs(page=1, page_size=10, genre="Rock", cache_directory="test_requests")

        # Verify that requests.get is not called
        mock_get.assert_not_called()

        # Verify that cached data is returned
        self.assertEqual(songs, response_data['data'])

        # Clean up: remove the cache file
        os.remove(cache_filename)

    @patch('songs.requests.get')
    def test_fetch_songs_not_cached(self, mock_get):
        # Prepare mocked response data
        response_data = {'data': [{'songId': 1, 'songName': 'Song 1'}, {'songId': 2, 'songName': 'Song 2'}]}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = response_data
        mock_get.return_value = mock_response

        # Call the fetch_songs method
        songs = fetch_songs(page=1, page_size=10, genre="Rock", cache_directory="test_requests")

        # Verify that requests.get is called
        mock_get.assert_called_once()

        # Verify that correct data is returned
        self.assertEqual(songs, response_data['data'])


if __name__ == '__main__':
    unittest.main()
