# sort array by length of elements

def sort_by_length(arr: list) -> list:
    return sorted(arr, key=len)

def main():
    print(sort_by_length(["a", "ccc", "dddd", "bb"]))
    print(sort_by_length(["apple", "pie", "shortcake"]))
    print(sort_by_length(["may", "april", "september", "august"]))


if __name__ == "__main__":
    main()

# Path: test_app.pys