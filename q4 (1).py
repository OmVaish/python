def digitToSet(number):
    if number < 10:
        return "Invalid number"
    else:
        return set(str(number))

def main():
    print("Enter a number(>=10): ")
    number = int(input())
    print(digitToSet(number))

if __name__ == "__main__":
    main()