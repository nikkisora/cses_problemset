'''

CSES - Permutations



Time limit: 1.00 s
Memory limit: 512 MB

A permutation of integers 1,2,...,n is called beautiful if there are no adjacent elements whose difference is 1.


Given n, construct a beautiful permutation if such a permutation exists.

Input


The only input line contains an integer n.

Output


Print a beautiful permutation of integers 1,2,...,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".

Constraints

1 <= n <= 10^6

Example 1


Input:
5


Output:
4 2 5 3 1

Example 2


Input:
3


Output:
NO SOLUTION 
'''

n = int(input())

if 1 < n < 4:
    print('NO SOLUTION')
else:
    for i in range(1, n, 2):
        print(i+1, end=' ')
    for i in range(0, n, 2):
        print(i+1, end=' ')