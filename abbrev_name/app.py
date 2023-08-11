def abbrev_name(name):
    name = name.split(" ")
    name = name[0][0].upper() + "." + name[1][0].upper()
    return name

def main():
    name = "Alfred Neuman"
    print(abbrev_name(name))

if __name__ == "__main__":
    main() # "A.N" 