'''

CSES - Another Game



Time limit: 1.00 s
Memory limit: 512 MB

There are n heaps of coins and two players who move alternately. On each move, a player selects some of the nonempty heaps and removes one coin from each heap. The player who removes the last coin wins the game.

Your task is to find out who wins if both players play optimally.

Input

The first input line contains an integer t: the number of tests. After this, t test cases are described:

The first line contains an integer n: the number of heaps.

The next line has n integers x_1,x_2,...,x_n: the number of coins in each heap.

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
3
1 2 3
2
2 2
4
5 5 4 5

Output:
first
second
first 
'''