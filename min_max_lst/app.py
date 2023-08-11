# Task
# Write a function that returns both the minimum and
# maximum number of the given list/array.

def min_max(lst: list[int]) -> list[int]:
    results = []
    results.append(min(lst))
    results.append(max(lst))
    return results


def main():
    print(min_max([1, 2, 3, 4, 5]))  # [1, 5]
    print(min_max([2334454, 5]))  # [5, 2334454]
    print(min_max([1]))  # [1, 1]
    # [-4, 6925]
    print(min_max([1, -4, 94, 120, 4945, 25, 341, 94, 5425, 42, 6925,]))


if __name__ == "__main__":
    main()

# Path: app.py
