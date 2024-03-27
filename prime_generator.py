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
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        p = 2
        while p ** 2 <= n:
            if primes[p]:
                for i in range(p ** 2, n + 1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n + 1) if primes[i]]

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


if __name__ == '__main__':
    PrimeGenerator.main()
