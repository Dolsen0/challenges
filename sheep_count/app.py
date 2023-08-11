def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count


def main():
    array1 = [True,  True,  True,  False, False, True,  True,  True, False]
    print(count_sheeps(array1)) # 6


if __name__ == '__main__':
    main()
