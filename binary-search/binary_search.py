def binary_search(number, numbers):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if number < numbers[mid]:
            high = mid - 1
        elif number > numbers[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    numbers_list = [-2, 1, 3, 5, 6, 12, 20]
    num = 12
    index = binary_search(num, numbers_list)
    if index != -1:
        print(f"Index of {num} is: {index}")
    else:
        print(f"{num} not found")
