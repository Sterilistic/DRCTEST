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


if __name__ == '__main__':
    
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    

    primes = prime_generator(start, end)

    print(primes)