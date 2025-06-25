def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    output = []
    element = "*" * n
    for _ in range(n):
        output.append(element)
    return output


if __name__ == "__main__":
    print(generate_square(3))
    print(generate_square(5))

# Output
# ['***', '***', '***']
# ['*****', '*****', '*****', '*****', '*****']
