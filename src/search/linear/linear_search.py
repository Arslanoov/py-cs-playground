from typing import List


# Time Complexity: O(n)
def linear_search(arr: List, find_item) -> int:
    for index, item in enumerate(arr):
        if item == find_item:
            return index

    return -1
