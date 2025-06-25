def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows for the upper part of the diamond.

    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    output = []
    j = n - 1
    for i in range(1, 2 * n, 2):
        starred_elements = "*" * (i)
        row = (" " * j) + starred_elements + (" " * j)
        output.append(row)
        j -= 1

    last = len(output) - 1
    for i in range(last - 1, -1, -1):
        output.append(output[i])
    return output


if __name__ == "__main__":
    print(generate_diamond(3))
    print(generate_diamond(5))

# Output
# ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
# ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
