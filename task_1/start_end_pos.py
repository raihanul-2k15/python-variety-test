# my own implementation of binary search
# I'm aware that there's a builtin function (bisect module)
# but I'll not use it
def binary_search(arr, x, l=0, r=None):
    r = len(arr) if r is None else r
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l


# function to find start and end pos of a target in sorted array
def start_end_pos(arr, value):
    n = len(arr)
    start = binary_search(arr, value)

    if start == n or arr[start] != value:
        return [-1, -1]

    end = binary_search(arr, value + 1, start, n) - 1
    return [start, end]


# some sample cases to test the function
output = start_end_pos([5, 7, 7, 9, 9, 10], 9)
print(output)
output = start_end_pos([5, 7, 7, 8, 8, 10], 6)
print(output)
