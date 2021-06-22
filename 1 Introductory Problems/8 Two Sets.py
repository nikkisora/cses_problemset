'''

CSES - Two Sets



Time limit: 1.00 s
Memory limit: 512 MB

Your task is to divide the numbers 1,2,...,n into two sets of equal sum.

Input


The only input line contains an integer n.

Output


Print "YES", if the division is possible, and "NO" otherwise.


After this, if the division is possible, print an example of how to create the sets. First, print the number of elements in the first set followed by the elements themselves in a separate line, and then, print the second set in a similar way.

Constraints

 1 <= n <= 10^6

Example 1


Input:
7


Output:
YES

4

1 2 4 7

3

3 5 6

Example 2


Input:
6


Output:
NO 
'''

n = int(input())
l1 = list()
l2 = list()
if n%2:
    if (n-1)//2%2:
        for i in range(1, (n-1)//2+1):
            if i%2:
                l1.extend([i, n-i])
            else:
                l2.extend([i, n-i])
        l2.append(n)
else:
    if not n//2%2:
        for i in range(1, n//2+1):
            if i%2:
                l1.extend([i, n-i+1])
            else:
                l2.extend([i, n-i+1])
                
if l1:
    print('YES')
    print(len(l1))
    print(*l1, sep=' ')
    print(len(l2))
    print(*l2, sep=' ')
else:
    print('NO')
                