/*
 A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

 a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

*/
import Foundation


func main() {
    for a in 1...1000 {

        for b in stride(from: a, through: (1000-a), by: 1) {
            let c = 1000 - (a+b)
            if (a * a + b * b == c * c) {
                print(a * b * c)
            }
        }
    }
}


main()