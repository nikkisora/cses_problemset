'''

CSES - One Bit Positions



Time limit: 1.00 s
Memory limit: 512 MB

You are given a binary string of length n and your task is to calculate for every k between 1 ... n-1 the number of ways we can choose two positions i and j such that i-j=k and there is a one-bit at both positions.

Input

The only input line has a string that consists only of characters 0 and 1.

Output

For every distance k between 1... n-1 print the number of ways we can choose two such positions.

Constraints

2 <= n <= 2 * 10^5

Example

Input:
1001011010

Output:
1 2 3 0 2 1 0 1 0 
'''