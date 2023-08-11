#   Check if a list contains an element

def check(seq: list, elem: str) -> bool:
    if elem in seq:
        return True
    else:
        return False

def main():
    print(check([1, 2, 3], 1))  # True
    print(check([1, 2, 3], 4))  # False
    print(check(['a', 'b', 'c'], 'a'))  # True
    print(check(['a', 'b', 'c'], 'd'))  # False


if __name__ == '__main__':
    main()