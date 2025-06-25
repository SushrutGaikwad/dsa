def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.

    Parameters:
    n (int): The height of the triangle.

    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    output = []
    for i in range(1, n + 1):
        row = f"{i}" * i
        output.append(row)
    return output


if __name__ == "__main__":
    print(generate_number_triangle(1))
    print(generate_number_triangle(3))
    print(generate_number_triangle(5))

# Output
# ['1']
# ['1', '22', '333']
# ['1', '22', '333', '4444', '55555']
