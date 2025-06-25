def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the sandglass.

    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    output = []
    j = (2 * n) - 1
    for i in range(n):
        starred_elements = "*" * j
        row = (" " * i) + starred_elements + (" " * i)
        output.append(row)
        j -= 2

    second_last_idx = len(output) - 2
    for i in range(second_last_idx, -1, -1):
        output.append(output[i])
    return output


if __name__ == "__main__":
    print(generate_sandglass(3))
    print(generate_sandglass(4))

# Output
# ['*****', ' *** ', '  *  ', ' *** ', '*****']
# ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
