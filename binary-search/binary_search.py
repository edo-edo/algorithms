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


def binary_search_dec(element, elements):
    low = 0
    high = len(elements) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if element < elements[mid]:
            low = mid + 1
        elif element > elements[mid]:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    elements_list = [-2, 1, 3, 5, 6, 12, 20]
    elements_list_dec = [20, 12, 6, 5, 3, 1, -2]
    ELEMENT = 12
    index = binary_search(ELEMENT, elements_list)
    index_dec_list = binary_search_dec(ELEMENT, elements_list_dec)

    print(elements_list, 'Order by asc')
    if index != -1:
        print(f"Index of {ELEMENT} is: {index}")
    else:
        print(f"{ELEMENT} not found")

    print(elements_list_dec, 'Order by dec')
    if index_dec_list != -1:
        print(f"Index of {ELEMENT} is: {index_dec_list}")
    else:
        print(f"{ELEMENT} not found")
