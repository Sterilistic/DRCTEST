import sys
import unittest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

class TestPrimeGenerator(unittest.TestCase):
    
    def test_is_prime_with_prime_numbers(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        for prime in primes:
            self.assertTrue(is_prime(prime), f"{prime} should be prime")

    def test_is_prime_with_non_prime_numbers(self):
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15]
        for non_prime in non_primes:
            self.assertFalse(is_prime(non_prime), f"{non_prime} should not be prime")

    def test_prime_generator_with_range(self):
        self.assertEqual(prime_generator(1, 15), [2, 3, 5, 7, 11, 13])
        self.assertEqual(prime_generator(-1, -10), [])


    def test_prime_generator_with_empty_range(self):
        self.assertEqual(prime_generator(10, 10), [])
        self.assertEqual(prime_generator(14, 16), [])

    def test_prime_generator_with_single_prime_number(self):
        expected_primes = [11]
        self.assertEqual(prime_generator(10, 12), expected_primes)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python prime_generator.py <start> <end>")
        sys.exit(1)
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start < 0 or end < 0:
        print("Invalid range. Start and end must be positive integers.")
        sys.exit(1)
    
    if start > end: # Swap start and end if start is greater than end
        start, end = end, start

    primes = prime_generator(start, end)
    print("Prime numbers between {} and {}: {}".format(start, end, primes))


