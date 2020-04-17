### A simple concept of Binary Search ###
# Using both iterative and recursive methods #

data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
target = 4

# Linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative Binary Search
def binary_search_iterative(data, target):
    # Assume data list is sorted
    low = 0              # index of first element
    high = len(data) - 1 # index of last element

    while low <= high:
        mid = (low + high) // 2   # middle element of list
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1
        print("Low: {}, Mid: {}, High: {}".format(low, mid, high))

    return False

# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    # Check if low point is greater than high point
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, (mid - 1))
        else:
            return binary_search_recursive(data, target, (mid + 1), high)

print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data) - 1))