// 2520 is the smallest number that can be divided by each of the numbers from 1 
// to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers 
// from 1 to 20?

#include <iostream>
using namespace std;

int divider(int divideTo) {
    bool resultNotFound = true;
    int testingNumber = 20;
    int result = 0;

    while (resultNotFound) {
        for(int i = divideTo - 1; i > 1; i--) {

            if (testingNumber % i == 0) {
                if(i == 2) {
                    resultNotFound = false;
                    result = testingNumber;

                }
            } else {
                break;
            }
        }
        testingNumber = testingNumber + 20;
    }


    cout << result << " is the smallest number.";
    return result;
}

int main() {
    divider(20);
}
