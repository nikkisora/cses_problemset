'''

CSES - Nim Game I



Time limit: 1.00 s
Memory limit: 512 MB

There are n heaps of sticks and two players who move alternately. On each move, a player chooses a non-empty heap and removes any number of sticks. The player who removes the last stick wins the game.

Your task is to find out who wins if both players play optimally.

Input

The first input line contains an integer t: the number of tests. After this, t test cases are described:

The first line contains an integer n: the number of heaps.

The next line has n integers x_1,x_2,...,x_n: the number of sticks in each heap.

Output

For each test case, print "first" if the first player wins the game and "second" if the second player wins the game.

Constraints

1 <= t <= 2 * 10^5
1 <= n <= 2 * 10^5
1 <= x_i <= 10^9
the sum of all n is at most 2 * 10^5

Example

Input:
3
4
5 7 2 5
2
4 1
3
3 5 6

Output:
first
first
second 
'''