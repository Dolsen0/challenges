# Given a year, return the century it is in.

def century(year: int) -> int:
    if year <= 100:
        return 1
    elif year % 100 == 0:
        return year / 100
    else:
        result = ((year / 100) + 1)
        return int(result)


def main():
    print(century(1705))
    print(century(1900))
    print(century(1601))
    print(century(356))


if __name__ == "__main__":
    main()
