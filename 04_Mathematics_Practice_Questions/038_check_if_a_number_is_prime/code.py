def is_prime(n):
    """
    Function to check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(is_prime(5))
    print(is_prime(4))

# Output
# True
# False
