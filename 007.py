# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?
from itertools import count
import math

def isItPrime(counter, foundPrimes):
    for num in range(int(math.sqrt(counter) +1), 0, -1):

        if(counter % num == 0):
            return (counter+1), foundPrimes

        elif(num == 2):
            counter = counter + 1
            foundPrimes = foundPrimes +1
            return counter, foundPrimes
        



def findTheNthPrime(n):
    foundPrimes = 1
    counter = 2
    while(n > foundPrimes):
        #counter, foundPrimes = isItPrime(counter, foundPrimes)
        counter, foundPrimes = isItPrime(counter, foundPrimes)
        
    print(counter-1)

findTheNthPrime(10001)


