// Euclid’s algorithm for finding the greatest common divisor of
// two numbers
#include <iostream>
using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    int r = a % b;
    return gcd(b, r);
}

int main() {
    int x, y;
    cout << "Enter a first number: ";
    cin >> x;
    cout << "Enter a second number: ";
    cin >> y;
    cout << "Answer is: " << gcd(x, y);
}

