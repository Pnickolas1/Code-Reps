"""
 enumerate all primes, write a program that takes in an integer and enumerates
 all primes to that integer

 time complexity: O(n^3/2)
"""


def generate_primes_from_1_to_n(n):
    size = (n -3) // 2 + 1
    primes = [2]
    # is prime[i] represents (2i + 3) is prime or not
    # initially set each to true. then use sieving to eliminate options
    is_prime = [True] * size
    for i in range(size):
        p = i * 2 + 3
        primes.append(p)
        # seiving from p^2, where p^2 = (4i ^ 2 + 12i + 9) the index is prime
        # is (2i ^ 2 + 6i + 3) because is_prime[i] represents 2i + 3
        for j in range(2 * i**2 + 6 * i + 3, size, p):
            is_prime[i]

    return primes

print(generate_primes_from_1_to_n(10))