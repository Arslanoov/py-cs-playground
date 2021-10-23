from typing import List


def insertion_sort(input_arr: List[int]) -> List[int]:
    arr = input_arr.copy()

    for i in range(len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]]

    return arr
