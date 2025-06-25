def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.

    Parameters:
    n (int): The number of even numbers to sum.

    Returns:
    int: The sum of the first n even natural numbers.
    """
    num = 2
    sum = 0
    for _ in range(n):
        sum += num
        num += 2
    return sum


if __name__ == "__main__":
    print(sum_of_even_numbers(3))
    print(sum_of_even_numbers(5))

# Output
# 12
# 30
