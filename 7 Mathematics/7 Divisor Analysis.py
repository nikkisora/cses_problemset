'''

CSES - Divisor Analysis



Time limit: 1.00 s
Memory limit: 512 MB

Given an integer, your task is to find the number, sum and product of its divisors. As an example, let us consider the number 12:
 the number of divisors is 6 (they are 1, 2, 3, 4, 6, 12)
 the sum of divisors is 1+2+3+4+6+12=28
 the product of divisors is 1 * 2 * 3 * 4 * 6 * 12 = 1728

Since the input number may be large, it is given as a prime factorization.

Input

The first line has an integer n: the number of parts in the prime factorization.

After this, there are n lines that describe the factorization. Each line has two numbers x and k where x is a prime and k is its power.

Output

Print three integers modulo 10^9+7: the number, sum and product of the divisors.

Constraints

1 <= n <= 10^5
2 <= x <= 10^6
each x is a distinct prime
1 <= k <= 10^9

Example

Input:
2
2 2
3 1

Output:
6 28 1728 
'''