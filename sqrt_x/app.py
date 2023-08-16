def mySqrt(x: int) -> int:
    start = 2
    end = x
    while start <= end:
        middle = start + ((end - start)// 2)
        if middle * middle == x:
            return middle
        elif middle * middle < x:
            start = middle + 1
        else:
            end = middle - 1
    return end

# O(log n) time complexity
# O(1) space complexity