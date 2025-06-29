def is_even(n):
    """
    Function to check if a number is even.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is even, False otherwise.
    """
    return n % 2 == 0


if __name__ == "__main__":
    print(is_even(4))
    print(is_even(7))

# Output
# True
# False
