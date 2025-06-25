def find_largest(numbers):
    largest_num = numbers[0]
    for number in numbers:
        if number > largest_num:
            largest_num = number
    return largest_num


if __name__ == "__main__":
    print(find_largest([3, 8, 2, 10, 5]))
    print(find_largest([-5, -10, -2, -1, -7]))

# Output
# 10
# -1
