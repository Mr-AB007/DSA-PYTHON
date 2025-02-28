def longest_fibo(arr: list) -> int:
    """
    Function to find the longest Fibonacci-like subsequence in a given sorted list.

    A Fibonacci-like subsequence is defined as a sequence where:
    - The sequence consists of at least 3 numbers.
    - Each number is the sum of the two preceding numbers.

    Args:
    arr (list): A list of unique, increasing integers.

    Returns:
    int: The length of the longest Fibonacci-like subsequence or 0 if none found.
    """

    n = len(arr)  # Get the size of the array
    arrset = set(arr)  # Convert the list to a tuple for quick lookup
    max_len = 2  # Tracks the maximum Fibonacci-like sequence length found

    # Outer loop: Select the first number of the sequence
    for i in range(n - 1):

        # Optimization: Break if extending the sequence is impossible
        if arr[i] * 1.618 ** (max_len - 1) > arr[n - 1]:
            break

        # Inner loop: Select the second number of the sequence
        for j in range(i + 1, n):

            # Another early termination condition to optimize performance
            if arr[j] * 1.618 ** (max_len - 2) > arr[n - 1]:
                break

            # Start a Fibonacci-like sequence with arr[i] and arr[j]
            a = arr[i]  # First element
            b = arr[j]  # Second element
            length = 2  # The sequence starts with two elements

            # Extend the sequence as long as the next number exists in the tuple
            while a + b in arrset:
                b = a + b  # Compute the next Fibonacci number
                a = b - a  # Update 'a' (swap without extra variable)
                length += 1  # Increase sequence length

            # Update the maximum length found
            max_len = max(max_len, length)

    # If no valid sequence is found (i.e., max length remains 2), return 0
    return max_len if max_len > 2 else 0


print(longest_fibo([1,2,3,4,5,6,7,8])) # putput: 5