def move(position, roll):
    roll = roll * 2
    position = position + roll
    return position


def main():
    print(move(2, 5))

if __name__ == '__main__':
    main()