def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    output = []
    if n == 1:
        return ["*"]

    first_row = "*" * n
    output.append(first_row)
    for i in range(n - 3, 0, -1):
        middle_row = "*" + (" " * i) + "*"
        output.append(middle_row)
    second_last_row = "**"
    last_row = "*"
    output.append(second_last_row)
    output.append(last_row)
    return output


if __name__ == "__main__":
    print(generate_hollow_inverted_right_angled_triangle(1))
    print(generate_hollow_inverted_right_angled_triangle(4))
    print(generate_hollow_inverted_right_angled_triangle(5))

# Output
# ['*']
# ['****', '* *', '**', '*']
# ['*****', '*  *', '* *', '**', '*']
