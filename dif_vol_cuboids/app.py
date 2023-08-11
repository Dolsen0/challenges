def find_difference(a: int, b: int) -> int:
    nums_a = 1
    nums_b = 1

    for i in a:
        nums_a = nums_a * i
    for i in b:
        nums_b = nums_b * i
    return abs(nums_a - nums_b)


def main():
    print(find_difference([3, 2, 5], [1, 4, 4]))    # 14
    print(find_difference([9, 7, 2], [5, 2, 2]))    # 106
    print(find_difference([11, 2, 5], [1, 10, 8]))  # 30


if __name__ == "__main__":
    main()
