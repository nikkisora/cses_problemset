'''

CSES - Weird Algorithm



Time limit: 1.00 s
Memory limit: 512 MB

Consider an algorithm that takes as input a positive integer n. If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one. The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:

 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Your task is to simulate the execution of the algorithm for a given value of n.

Input


The only input line contains an integer n.

Output


Print a line that contains all values of n during the algorithm.

Constraints

1 <= n <= 10^6

Example


Input:
3


Output:
3 10 5 16 8 4 2 1 
'''

n = input()

if n.isnumeric():
    n = int(n)
    while n != 1:
        print(int(n), end=' ')
        if n%2:
            n=n*3+1
        else:
            n/=2
    print(1)