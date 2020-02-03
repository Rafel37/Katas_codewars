def binary_array_to_number(arr):
    total = 0
    n = len(arr) - 1
    for i in range(len(arr)):
       total += arr[i] * 2**(n - i)
    return total