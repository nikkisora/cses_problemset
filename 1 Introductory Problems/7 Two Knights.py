'''

CSES - Two Knights



Time limit: 1.00 s
Memory limit: 512 MB

Your task is to count for k=1,2,...,n the number of ways two knights can be placed on a k * k chessboard so that they do not attack each other.

Input


The only input line contains an integer n.

Output


Print n integers: the results.

Constraints

1 <= n <= 10000

Example


Input:
8


Output:
0

6

28

96

252

550

1056

1848 
'''
import math

n = int(input())

for k in range(1, n+1):
    combinations = (k*k-1) * (k*k)//2
    combinations -= 4 * (k-1) * (k-2)
     
    print(combinations)