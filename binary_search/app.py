from typing import List

def search(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = start + ((end - start) >> 1)
        if target < nums[middle]:
            end = middle - 1
        elif target > nums[middle]:
            start = middle + 1
        else:
            return middle
    return -1

print(search([1, 2, 3, 4, 5, 8, 10, 12, 15, 19, 22, 30, 34, 37, 47, 66], 22))
