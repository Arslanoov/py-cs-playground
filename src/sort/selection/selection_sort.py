from typing import List


# Time Complexity: O(n^2)
def selection_sort(input_arr: List[int]) -> List[int]:
    arr = input_arr.copy()

    for i in range(len(arr) - 1):
        smallest = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j

        if smallest != i:
            [arr[i], arr[smallest]] = [arr[smallest], arr[i]]

    return arr
