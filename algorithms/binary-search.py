def binary_search(arr, x, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if high >= low:
        mid = high + low // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, x, low, mid - 1)
        else:
            return binary_search(arr, x, mid + 1, high)

    else:
        return -1
