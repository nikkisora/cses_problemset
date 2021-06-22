'''

CSES - Prime Multiples



Time limit: 1.00 s
Memory limit: 512 MB

You are given k distinct prime numbers a_1,a_2,...,a_k and an integer n.

Your task is to calculate how many of the first n positive integers are divisible by at least one of the given prime numbers.

Input

The first input line has two integers n and k.

The second line has k prime numbers a_1,a_2,...,a_k.

Output

Print one integer: the number integers within the interval 1,2,...,n that are divisible by at least one of the prime numbers.

Constraints

 1 <= n <= 10^{18}
 1 <= k <= 20
 2 <= a_i <= n

Example

Input:
20 2
2 5

Output:
12

Explanation: the 12 numbers are 2,4,5,6,8,10,12,14,15,16,18,20.    
'''