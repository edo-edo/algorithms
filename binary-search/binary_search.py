def binary_search(element, elements):
    low = 0
    high = len(elements) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if element < elements[mid]:
            high = mid - 1
        elif element > elements[mid]:
            low = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    elements_list = [-2, 1, 3, 5, 6, 12, 20]
    ELEMENT = 12
    index = binary_search(ELEMENT, elements_list)
    if index != -1:
        print(f"Index of {ELEMENT} is: {index}")
    else:
        print(f"{ELEMENT} not found")
