import unittest
import os
from scrape_songs import write_to_csv  # Importing your module containing the method


class TestWriteToCSV(unittest.TestCase):
    def setUp(self):
        # Create a test directory for outputs
        self.output_directory = "test_outputs"
        os.makedirs(self.output_directory, exist_ok=True)

    def tearDown(self):
        # Clean up the test directory for outputs
        for filename in os.listdir(self.output_directory):
            file_path = os.path.join(self.output_directory, filename)
            os.remove(file_path)
        os.rmdir(self.output_directory)

    def test_write_to_csv(self):
        # Sample songs data
        songs = [
            {
                'songId': 1,
                'songName': 'Song 1',
                'artistName': 'Artist 1',
                'albumName': 'Album 1',
                'genre': 'Genre 1',
                'songYear': 2022,
                'songLength': '3:45',
                'hasUGCGuitarArrangement': True,
                'hasUGCBassArrangement': False,
                'hasUGCPianoArrangement': True,
                'hasOfficialGuitarArrangement': False,
                'hasOfficialBassArrangement': True,
                'hasOfficialPianoArrangement': False,
            },
            {
                'songId': 2,
                'songName': 'Song 2',
                'artistName': 'Artist 2',
                'albumName': 'Album 2',
                'genre': 'Genre 2',
                'songYear': 2023,
                'songLength': '4:30',
                'hasUGCGuitarArrangement': False,
                'hasUGCBassArrangement': True,
                'hasUGCPianoArrangement': False,
                'hasOfficialGuitarArrangement': True,
                'hasOfficialBassArrangement': False,
                'hasOfficialPianoArrangement': True,
            }
        ]

        # Create a temporary file path
        temp_file_name = 'test_output.csv'
        temp_file_path = os.path.join(self.output_directory,'test_output.csv')

        # Call the method with the temporary file path
        write_to_csv(songs, temp_file_name, output_dir=self.output_directory)

        # Check if the file was created and contains expected content
        self.assertTrue(os.path.exists(temp_file_path))

        with open(temp_file_path, 'r') as file:
            csv_content = file.read()

        # Verify if the content matches the expected CSV format
        expected_csv_content = """Song ID,Song Name,Artist,Album,Genre,Year,Duration,hasUGCGuitarArrangement,hasUGCBassArrangement,hasUGCPianoArrangement,hasOfficialGuitarArrangement,hasOfficialBassArrangement,hasOfficialPianoArrangement\n1,Song 1,Artist 1,Album 1,Genre 1,2022,3:45,True,False,True,False,True,False\n2,Song 2,Artist 2,Album 2,Genre 2,2023,4:30,False,True,False,True,False,True\n"""
        self.assertEqual(csv_content, expected_csv_content)

        # Clean up: Remove the temporary file
        os.remove(temp_file_path)


if __name__ == '__main__':
    unittest.main()
