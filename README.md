Prime Number Generator Coding Exercise
Python Edition
Overview:

Your task is to use test-driven development to implement a prime number generator that
returns prime numbers in a given range (inclusive of the endpoints). You must
implement the generator specified below. You may also create any other methods,
interfaces and/or classes that you deem necessary to complete the project. You should
also develop a small main program to drive your generator and to allow the user to
specify the prime number range via the command line. To successfully complete the
exercise, all unit tests must pass as well as provide 100% code coverage.
Notes
• You may not use the isprime method from sympy, we want to see you implement
a python generator that returns primes on your own.
The code should handle inverse ranges such that 1-10 and 10-1 are equivalent.
• Ensure that you run a test against the range 7900 and 7920 (valid primes are
7901, 7907, 7919).

Generator function signature

`def prime_generator(start:int , end:int)`

Primality checker signature

`def is_prime(value:int)`


Definition (from wikipedia):
In mathematics, a prime number (or a prime) is a natural number which has exactly
two distinct natural number divisors: 1 and itself. The first twenty-six prime numbers are:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
97, 101

How to run, 
`pushpendrakumartiwari@Pushpendras-MacBook-Pro DRCTEST % python3 prime_generator.py 14 19
Prime numbers between 14 and 19: [17, 19]
`

Test coverage check, 
```
pushpendrakumartiwari@Pushpendras-MacBook-Pro DRCTEST % coverage run -m pytest test_interface_prime_generator.py -v 
============================================================== test session starts ===============================================================
platform darwin -- Python 3.10.8, pytest-8.1.1, pluggy-1.4.0 -- /usr/local/opt/python@3.10/bin/python3.10
cachedir: .pytest_cache
rootdir: /Users/pushpendrakumartiwari/work/DRCTEST
plugins: anyio-3.6.2
collected 9 items                                                                                                                                

test_interface_prime_generator.py::TestPrimeGenerator::test_generate_primes_with_empty_range PASSED                                        [ 11%]
test_interface_prime_generator.py::TestPrimeGenerator::test_generate_primes_with_range PASSED                                              [ 22%]
test_interface_prime_generator.py::TestPrimeGenerator::test_generate_primes_with_single_prime_number PASSED                                [ 33%]
test_interface_prime_generator.py::TestPrimeGenerator::test_is_prime_with_non_prime_numbers PASSED                                         [ 44%]
test_interface_prime_generator.py::TestPrimeGenerator::test_is_prime_with_prime_numbers PASSED                                             [ 55%]
test_interface_prime_generator.py::TestUserInput::test_insufficient_arguments PASSED                                                       [ 66%]
test_interface_prime_generator.py::TestUserInput::test_invalid_input_negative_numbers PASSED                                               [ 77%]
test_interface_prime_generator.py::TestUserInput::test_invalid_input_non_numeric PASSED                                                    [ 88%]
test_interface_prime_generator.py::TestUserInput::test_valid_input PASSED                                                                  [100%]

=============================================================== 9 passed in 0.04s ================================================================
```