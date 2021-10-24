from typing import List
from math import floor


# Time Complexity: O(log(n))
def binary_search(arr: List, find_item: int) -> int:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        middle: int = left + floor((right - left) / 2)
        if arr[middle] < find_item:
            right = middle - 1
        elif arr[middle] == find_item:
            return middle
        else:
            left = middle + 1

    return -1
