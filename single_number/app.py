from typing import List

def singleNumber(nums: List[int]) -> int:
    dict = {}
    for num in nums:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1
    for value in dict:
        if dict[value] == 1:
            return value


print(singleNumber([1, 2, 3, 3, 1, 5, 4, 4, 5]))  # [1,2,3,4,5]
print(singleNumber([1, 2, 3, 3, 1, 5, 4, 4, 5, 6, 6, 7, 7]))  # [1,2,3,4,5,6,7]