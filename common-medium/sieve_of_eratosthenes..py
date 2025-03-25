
"""
    Problem Statement:
    Given an integer n, return the number of prime numbers that are strictly less than n.

    Example:
    Input: n = 10
    Output: 4
    Explanation: There are four prime numbers less than 10, which are 2, 3, 5, and 7.

    Algorithm Used: Sieve of Eratosthenes

    Time Complexity: O(n log log n) - Efficiently marks non-prime numbers.
    Space Complexity: O(n) - Uses a boolean list of size n.
    """

def count_prime_arr_false(n: int) -> int:

    # Edge case: If n is less than or equal to 2, no prime numbers exist
    if n <= 2:
        return 0

    # Boolean list initialized to False (False means prime, True means non-prime)
    arr = [False] * n
    arr[0] = arr[1] = True  # 0 and 1 are not prime

    # Implementing the Sieve of Eratosthenes algorithm
    for i in range(2, int(n ** 0.5) + 1):  # Loop till sqrt(n)
        if not arr[i]:  # If i is prime (False means prime)
            for j in range(i * i, n, i):  # Mark multiples of i as non-prime
                arr[j] = True  # Mark non-prime numbers as True

    # Counting the number of prime numbers (counting False values)
    return arr.count(False)  # Count False values since they represent primes


def count_prime_arr_true(n: int) -> int:

    # Edge case: If n is less than or equal to 2, no prime numbers exist
    if n <= 2:
        return 0

    # Boolean list to track prime numbers, initialized to True
    arr = [True] * n
    arr[0] = arr[1] = False  # 0 and 1 are not prime

    # Implementing the Sieve of Eratosthenes algorithm
    for i in range(2, int(n ** 0.5) + 1):  # Loop till sqrt(n)
        if arr[i]:  # If i is prime
            for j in range(i * i, n, i):  # Mark multiples of i as non-prime
                arr[j] = False

    # Counting the number of prime numbers
    return sum(arr)  # True values count as 1, False as 0

# Example usage:
print(count_prime_arr_false(10))  # Output: 4

# Example usage:
print(count_prime_arr_true(10))  # Output: 4
