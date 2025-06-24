def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The number of rows in the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    output = []
    iteration = 0
    for i in range(1, 2 * n, 2):
        iteration += 1
        row = "*" * i
        row = (" " * (n - iteration)) + row + (" " * (n - iteration))
        output.append(row)
    return output


print(generate_pyramid(1))

print(generate_pyramid(3))

print(generate_pyramid(5))

# Output
# ['*']
# ['  *  ', ' *** ', '*****']
# ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
