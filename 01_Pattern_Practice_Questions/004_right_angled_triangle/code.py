def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height and base of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    output = []
    for i in range(1, n + 1):
        row = "*" * i
        output.append(row)
    return output


print(generate_triangle(1))

print(generate_triangle(3))

print(generate_triangle(5))

# Output
# ['*']
# ['*', '**', '***']
# ['*', '**', '***', '****', '*****']
