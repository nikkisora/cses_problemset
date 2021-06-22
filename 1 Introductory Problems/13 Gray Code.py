'''

CSES - Gray Code



Time limit: 1.00 s
Memory limit: 512 MB

A Gray code is a list of all 2^n bit strings of length n, where any two successive strings differ in exactly one bit (i.e., their Hamming distance is one).


Your task is to create a Gray code for a given length n.

Input


The only input line has an integer n.

Output


Print 2^n lines that describe the Gray code. You can print any valid solution.

Constraints

1 <= n <= 16

Example


Input:
2


Output:
00

01

11

10 
'''

n = int(input())

for i in range(2**n):
    print(bin(i^(i>>1))[2:].rjust(n, '0'))