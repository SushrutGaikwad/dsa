def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.

    Parameters:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    output = []
    i = 1
    for row_num in range(n):
        row = []
        for element in range(i, i + row_num + 1):
            row.append(str(element))
            i += 1
        row = " ".join(row)
        output.append(row)
    return output


if __name__ == "__main__":
    print(generate_floyds_triangle(3))
    print(generate_floyds_triangle(5))

# Output
# ['1', '2 3', '4 5 6']
# ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']
