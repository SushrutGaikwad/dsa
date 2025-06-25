def calculate_y(slope, intercept, x):
    """
    Function to calculate the value of y using the slope-intercept form of a line.

    Parameters:
    slope (float): The slope of the line.
    intercept (float): The y-intercept of the line.
    x (float): The value of x for which y needs to be calculated.

    Returns:
    float: The calculated value of y.
    """
    return (slope * x) + intercept


if __name__ == "__main__":
    print(calculate_y(2, 3, 4))
    print(calculate_y(1.5, -2, 2))

# Output
# 11
# 1.0
