def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.

    Parameters:
    n (int): The height of the pyramid.

    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    output = []
    for i in range(1, n + 1):
        numbers = []
        for j in range(1, i + 1):
            numbers.append(" ".join(list(str(j))))
        output.append(" ".join(numbers))

    for i in range(n):
        output[i] = (" " * (n - i - 1)) + output[i] + (" " * (n - i - 1))

    return output


if __name__ == "__main__":
    print(generate_number_pyramid(1))
    print(generate_number_pyramid(4))
    print(generate_number_pyramid(3))

# Output
# ['1']
# ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
# ['  1  ', ' 1 2 ', '1 2 3']
