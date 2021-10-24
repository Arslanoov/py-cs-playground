from typing import List


# Time Complexity: O(n^2)
def bubble_sort(input_arr: List[int]) -> List[int]:
    arr = input_arr.copy()

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]

    return arr
