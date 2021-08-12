
def binary_search(element, low, high, elements):
    if high >= low:
        mid = low + (high - low) // 2
        if element < elements[mid]:
            return binary_search(element, low, high - 1, elements)
        if element > elements[mid]:
            return binary_search(element, low + 1, high, elements)
        return mid
    return -1


if __name__ == "__main__":
    elements_list = [-2, 1, 3, 5, 6, 12, 20]
    ELEMENT = 3
    index = binary_search(ELEMENT, 0, len(elements_list) - 1, elements_list)
    if index != -1:
        print(f"Index of {ELEMENT} is: {index}")
    else:
        print(f"{ELEMENT} not found")
