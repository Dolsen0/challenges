from typing import List


def two_sum(nums, target):
    dict = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in dict:
            return [dict[difference], i]
        else:
            dict[nums[i]] = i



            
print(two_sum([2,3,9,7,11,15], 9))  # [0, 1]
print(two_sum([3,2,4], 6))  # [1, 2]
print(two_sum([2,3,7,1,6,2], 9))    # [2, 4]

# Function that takes in an array of integers and a target integer
# time: O(n)
# space: O(n)

