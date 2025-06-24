def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the inverted pyramid.

    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    output = []
    iteration = 0
    for i in range(1, 2 * n, 2):
        iteration += 1
        row = "*" * ((2 * n) - i)
        row = (" " * (iteration - 1)) + row + (" " * (iteration - 1))
        output.append(row)
    return output


print(generate_inverted_pyramid(1))

print(generate_inverted_pyramid(3))

print(generate_inverted_pyramid(5))

# Output
# ['*']
# ['*****', ' *** ', '  *  ']
# ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
