def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.

    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.

    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    if n == 0:
        return 0
    if n < capacity:
        return 1
    if n % capacity != 0:
        return n // capacity + 1
    return n // capacity


if __name__ == "__main__":
    print(calculate_lift_rounds(10, 3))
    print(calculate_lift_rounds(7, 4))
    print(calculate_lift_rounds(1, 4))
    print(calculate_lift_rounds(0, 4))

# Output
# 4
# 2
# 1
# 0
