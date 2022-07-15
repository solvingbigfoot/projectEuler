// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143 ?
// The answer is 6857 

import Foundation

func isItPrime(number: Int) -> (Bool) {
    for num in stride(from: 2, to: Int(Float(number).squareRoot()), by: 1) {
        if number % num == 0 {
            return (false)
        }
    }
    return (true)
}

func main() {
    var trueOrFalse = false
    var numberTested  = 0
    let challengeNumber = 600851475143
    let squareRootNumber = Float(challengeNumber).squareRoot()

    testingLoop: for number in stride(from: Int(squareRootNumber), to: 3, by: -1) {

        if isItPrime(number: number) && (challengeNumber % number == 0) {
            numberTested = number
            trueOrFalse = true
            break testingLoop
        }
    }
    print(numberTested, "is a prime numer?")
    print(trueOrFalse)
}

main()