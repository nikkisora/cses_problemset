'''

CSES - Substring Reversals



Time limit: 1.00 s
Memory limit: 512 MB

Given a string, your task is to process operations where you reverse a substring of the string. What is the final string after all the operations?

Input

The first input line has two integers n and m: the length of the string and the number of operations. The characters of the string are numbered 1,2,...,n.

The next line has a string of length n that consists of characters A�Z.

Finally, there are m lines that describe the operations. Each line has two integers a and b: you reverse a substring from position a to position b.

Output

Print the final string after all the operations.

Constraints

 1 <= n, m <= 2 * 10^5
 1 <= a <= b <= n

Example

Input:
7 2
AYBABTU
3 4
4 7

Output:
AYAUTBB 
'''