from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1
    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    return start

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6,7,8,9,10,15,16,17,18], 8))  # 5
print(searchInsert([1,3,5,6,7,8,9,10,15,16,17,18], 12))  # 8


# big o
# time complexity: O(log n)
# space complexity: O(1)

