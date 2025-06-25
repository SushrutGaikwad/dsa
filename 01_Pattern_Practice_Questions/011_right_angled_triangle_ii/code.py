def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    output = []
    j = n - 1
    for i in range(1, n + 1):
        row = (" " * j) + ("*" * i)
        output.append(row)
        j -= 1
    return output


if __name__ == "__main__":
    print(generate_right_angled_triangle(4))
    print(generate_right_angled_triangle(3))

# Output
# ['   *', '  **', ' ***', '****']
# ['  *', ' **', '***']
