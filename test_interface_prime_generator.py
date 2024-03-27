import sys
import unittest
from unittest.mock import patch
from io import StringIO

import prime_generator


class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.prime_gen = prime_generator.PrimeGenerator()

    def test_is_prime_with_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            self.assertTrue(self.prime_gen.is_prime(prime), f"{prime} should be prime")

    def test_is_prime_with_non_prime_numbers(self):
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
        for non_prime in non_primes:
            self.assertFalse(self.prime_gen.is_prime(non_prime), f"{non_prime} should not be prime")

    def test_generate_primes_with_range(self):
        self.assertEqual(self.prime_gen.generate_primes(1, 15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(self.prime_gen.generate_primes(-1, -10), [])

    def test_generate_primes_with_empty_range(self):
        self.assertEqual(self.prime_gen.generate_primes(10, 10), [])
        self.assertEqual(self.prime_gen.generate_primes(14, 16), [])

    def test_generate_primes_with_single_prime_number(self):
        expected_primes = [11]
        self.assertEqual(self.prime_gen.generate_primes(10, 12), expected_primes)

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
