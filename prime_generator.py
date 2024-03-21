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