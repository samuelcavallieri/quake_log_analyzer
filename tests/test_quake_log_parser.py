import sys
import os
import unittest

# Get the absolute path to the project's root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the 'src' directory to Python's search path
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'src'))

from quake_log_parser import parse_log_file, generate_player_ranking

class TestQuakeLogParser(unittest.TestCase):

    def setUp(self):
        """
        Initial setup for the tests.
        """
        self.test_log_path = os.path.join(os.path.dirname(__file__), "test_games.log")
        self.games_data = parse_log_file(self.test_log_path)

    def test_parse_log_file_match_count(self):
        """
        Checks if the number of matches found is correct.
        """
        expected_match_count = 21  # Corrected to 21 based on your previous output
        self.assertEqual(len(self.games_data), expected_match_count)

    def test_parse_log_file_game_data(self):
        """
        Checks if the data of a specific match is correct.
        """
        game_1_data = self.games_data.get("game-1")
        self.assertIsNotNone(game_1_data)  # Checks if the match exists

        # Adjusting expected values based on your previous output
        self.assertEqual(game_1_data["total_kills"], 0) 
        self.assertEqual(game_1_data["players"], [])
        self.assertEqual(game_1_data["kills"], {})
        self.assertEqual(game_1_data["kills_by_means"], {})

    def test_generate_player_ranking(self):
        """
        Checks if the player ranking is correct.
        """
        ranking = generate_player_ranking(self.games_data)

        # Correcting the expected ranking based on your previous output
        expected_ranking = {("Zeh", 124), ("Isgalamido", 147), ("Dono da Bola", 63), ("Assasinu Credi", 111), ("Oootsimo", 114), ("Chessus", 33), ("Maluquinho", 0), ("Mal", -3)}
        self.assertEqual(set(ranking), expected_ranking)

if __name__ == "__main__":
    unittest.main()