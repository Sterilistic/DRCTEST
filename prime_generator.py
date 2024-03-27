import sys
import unittest

class PrimeGenerator:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def generate_primes(start, end):
        if start > end:
            start, end = end, start  # Swap start and end if start is greater than end
        primes = []
        for num in range(start, end + 1):
            if PrimeGenerator.is_prime(num):
                primes.append(num)
        return primes

    @staticmethod
    def main():
        if len(sys.argv) != 3:
            print("Usage: python prime_generator.py <start> <end>", file=sys.stderr)
            sys.exit(1)
        
        try:
            start = int(sys.argv[1])
            end = int(sys.argv[2])
        except ValueError:
            print("Invalid range. Start and end must be positive integers.", file=sys.stderr)
            sys.exit(1)

        if start < 0 or end < 0:
            print("Invalid range. Start and end must be positive integers.", file=sys.stderr)
            sys.exit(1)
        
        if start > end: # Swap start and end if start is greater than end
            start, end = end, start

        prime_gen = PrimeGenerator()
        primes = prime_gen.generate_primes(start, end)
        print("Prime numbers between {} and {}: {}".format(start, end, primes))


class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.prime_gen = PrimeGenerator()

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


if __name__ == '__main__':
    PrimeGenerator.main()
