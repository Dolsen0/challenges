from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
    start = 0
    end = len(letters) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if letters[mid] <= target:
            start = mid + 1
        elif letters[mid] > target:
            end = mid - 1
    return letters[start % len(letters)]


print(nextGreatestLetter(["c", "f", "j"], "a"))

# time complexity: O(log n)
# space complexity: O(1)