def calculate_distance(speed, time):
    """
    Function to calculate the distance traveled by a vehicle.

    Parameters:
    speed (float): The speed of the vehicle.
    time (float): The time the vehicle has traveled.

    Returns:
    float: The distance traveled by the vehicle.
    """
    return speed * time


if __name__ == "__main__":
    print(calculate_distance(60, 2))
    print(calculate_distance(50.5, 1.5))

# Output
# 120
# 75.75
