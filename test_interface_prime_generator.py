import sys
import unittest
from unittest.mock import patch
from io import StringIO

import prime_generator

class TestUserInput(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_valid_input(self, mock_stdout):
        with patch.object(sys, 'argv', ['prime_generator.py', '1', '15']):
            prime_generator.PrimeGenerator.main()
            expected_output = "Prime numbers between 1 and 15: [2, 3, 5, 7, 11, 13]\n"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    @patch('sys.stderr', new_callable=StringIO)
    def test_invalid_input_non_numeric(self, mock_stderr):
        with patch.object(sys, 'argv', ['prime_generator.py', 'a', '15']):
            with self.assertRaises(SystemExit):
                prime_generator.PrimeGenerator.main()
            self.assertIn("Invalid range. Start and end must be positive integers.", mock_stderr.getvalue().strip())

    @patch('sys.stderr', new_callable=StringIO)
    def test_invalid_input_negative_numbers(self, mock_stderr):
        with patch.object(sys, 'argv', ['prime_generator.py', '-5', '15']):
            with self.assertRaises(SystemExit):
                prime_generator.PrimeGenerator.main()
            self.assertIn("Invalid range. Start and end must be positive integers.", mock_stderr.getvalue().strip())

    @patch('sys.stderr', new_callable=StringIO)
    def test_insufficient_arguments(self, mock_stderr):
        with patch.object(sys, 'argv', ['prime_generator.py', '10']):
            with self.assertRaises(SystemExit):
                prime_generator.PrimeGenerator.main()
            self.assertIn("Usage: python prime_generator.py <start> <end>", mock_stderr.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
