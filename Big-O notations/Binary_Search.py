arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr.sort()
start_index = 0
end_index = len(arr) - 1
target = 5

def binary_search(arr, start_index, end_index, target):

    if start_index > end_index:
        return False

    mid_index = (start_index + end_index) // 2

    if arr[mid_index] == target:
        return mid_index

    elif arr[mid_index] > target:
        return binary_search(arr, start_index, mid_index - 1, target)

    else:
        return binary_search(arr, start_index, mid_index + 1, target)

print(binary_search(arr, start_index, end_index, target))