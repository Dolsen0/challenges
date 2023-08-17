from typing import List

def peakIndexInMountainArray(arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid

    return start










print(peakIndexInMountainArray([0,1,0]))  # 1
print(peakIndexInMountainArray([0,2,1,0]))  # 1
print(peakIndexInMountainArray([0,10,5,2]))  # 1
print(peakIndexInMountainArray([3,4,5,1]))  # 2
print(peakIndexInMountainArray([24,69,100,99,79,78,67,36,26,19]))  # 2