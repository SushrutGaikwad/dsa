def celsius_to_fahrenheit(C):
    """
    Function to convert temperature from Celsius to Fahrenheit.

    Parameters:
    C (float): The temperature in Celsius.

    Returns:
    float: The temperature in Fahrenheit.
    """
    F = ((9 * C) / 5) + 32
    return F


if __name__ == "__main__":
    print(celsius_to_fahrenheit(25))
    print(celsius_to_fahrenheit(0))

# Output
# 77.0
# 32.0
