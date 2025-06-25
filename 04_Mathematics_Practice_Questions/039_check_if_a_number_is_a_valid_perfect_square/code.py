def is_perfect_square(num):
    """
    Function to check if a number is a perfect square.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if num is a perfect square, False otherwise.
    """
    return int(num ** (0.5)) == num ** (0.5)


if __name__ == "__main__":
    print(is_perfect_square(16))
    print(is_perfect_square(14))

# Output
# True
# False
