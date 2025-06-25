def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.

    Parameters:
    n (int): The size of the square.

    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    output = []
    for i in range(n):
        if (i == 0) or (i == n - 1):
            row = "*" * n
            output.append(row)
        else:
            hollow_row = "*" + (n - 2) * " " + "*"
            output.append(hollow_row)
    return output


if __name__ == "__main__":
    print(generate_hollow_square(1))
    print(generate_hollow_square(2))
    print(generate_hollow_square(3))
    print(generate_hollow_square(5))


# Output

# ['*']
# ['**', '**']
# ['***', '* *', '***']
# ['*****', '*   *', '*   *', '*   *', '*****']
