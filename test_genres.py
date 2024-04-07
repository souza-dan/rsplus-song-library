import unittest
from unittest.mock import patch
from genres import get_genres


class TestGetGenres(unittest.TestCase):

    @patch('requests.get')
    def test_get_genres_success(self, mock_get):
        # Mocking the response from the API
        mock_response = {
            "data": [
                "Blues",
                "Children's Music",
                "Classical",
                "Comedy",
                "Country",
                "Electronic",
                "Folk",
                "Hip-Hop",
                "Holiday Music",
                "Jazz",
                "Latin",
                "Metal",
                "New Age",
                "Other",
                "Pop",
                "R&B",
                "Reggae",
                "Regional Music",
                "Rock",
                "Sacred Music",
                "Stage & Screen"
            ],
            "error": None,
            "notifications": [],
            "invalid": False,
            "valid": True
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the function to get the genres
        genres = get_genres()

        # Assert that the function returned the expected genres
        expected_genres = mock_response['data']
        self.assertEqual(genres, expected_genres)

    @patch('requests.get')
    def test_get_genres_failure(self, mock_get):
        # Mocking the response from the API with failure status code
        mock_get.return_value.status_code = 404

        # Call the function to get the genres
        genres = get_genres()

        # Assert that the function returned an empty list in case of failure
        self.assertEqual(genres, [])


if __name__ == '__main__':
    unittest.main()
