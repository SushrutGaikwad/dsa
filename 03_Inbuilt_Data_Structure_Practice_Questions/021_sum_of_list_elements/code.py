def sum_list(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum


if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4, 5]))
    print(sum_list([10, -5, 7, 8, -2]))

# Output
# 15
# 18
