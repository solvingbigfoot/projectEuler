# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

numberOfDigits = 3

# This function tests find out if the product of two numbers is a palindrome
def palindromeTest(num1, num2, result):
    temp = str(num1 * num2)
    if temp == temp[::-1]:
        if (num1 * num2) > result:
            result = num1 * num2
    return result
    
# this function finds the largest palindrome 
def findPalindromic(numberOfDigits):

    result = 0
    for num1 in range(10**numberOfDigits-1, 1, -1):
        #print(num1)
        for num2 in range(10**numberOfDigits-1, 100, -1):
            result = palindromeTest(num1, num2, result)
    print(result)



findPalindromic(numberOfDigits)