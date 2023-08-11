def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return((fahrenheit - 32) * 5/9)

def celsius_to_fahrenheit(celsius: float) -> float:
    return((celsius * 9/5) + 32)

def main():
    degrees = input("Enter temperature: ")
    try:
        degrees = float(degrees)
        print(f"{degrees}°F in Celsius is {fahrenheit_to_celsius(degrees)}°C")
        print(f"{degrees}°C in Fahrenheit is {celsius_to_fahrenheit(degrees)}°F")
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()