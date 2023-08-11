def area_or_perimeter(l , w):
    if l == w:
        return l * w
    else:
        return 2 *(l + w)


def main():
    print(area_or_perimeter(4, 4))

if __name__ == '__main__':
    main()