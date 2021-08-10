# Euclid’s algorithm for finding the greatest common divisor of
# two numbers
def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


if __name__ == "__main__":
    x = int(input("Enter a first number: "))
    y = int(input("Enter a second number: "))
    print("Answer is: ", gcd(x, y))
