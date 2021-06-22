'''

CSES - Required Substring



Time limit: 1.00 s
Memory limit: 512 MB

Your task is to calculate the number of strings of length n having a given string of length m as their substring. All strings consist of characters A�Z.

Input

The first input line has an integer n: the length of the final string.

The second line has a string of length m.

Output

Print the number of strings modulo 10^9+7.

Constraints

1 <= n <= 1000
1 <= m <= 100

Example

Input:
6
ABCDB

Output:
52

Explanation: The final string will be of the form ABCDBx or xABCDB where x is any character between A�Z.    
'''