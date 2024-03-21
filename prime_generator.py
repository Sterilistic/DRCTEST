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
    if start > end:
        start, end = end, start  # Swap start and end if start is greater than end
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

class TestPrimeGenerator(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertTrue(is_prime(11))
        # Test edge cases
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(32))
        self.assertFalse(is_prime(33))
        self.assertFalse(is_prime(100))
    
    def test_prime_generator(self):
        self.assertEqual(prime_generator(1, 10), [2, 3, 5, 7])
        self.assertEqual(prime_generator(20, 30), [23, 29])
        self.assertEqual(prime_generator(30, 20), [23, 29])
        self.assertEqual(prime_generator(7900, 7920), [7901, 7907, 7919])

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("Usage: python prime_generator.py <start> <end>")
        sys.exit(1)
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    if start < 0 or end < 0:
        print("Invalid range. Start and end must be positive integers.")
        sys.exit(1)
    

    primes = prime_generator(start, end)

    if start > end:
        start, end = end, start
    print("Prime numbers between {} and {}: {}".format(start, end, primes))


