'''

CSES - Coin Collector



Time limit: 1.00 s
Memory limit: 512 MB

A game has n rooms and m tunnels between them. Each room has a certain number of coins. What is the maximum number of coins you can collect while moving through the tunnels when you can freely choose your starting and ending room?

Input

The first input line has two integers n and m: the number of rooms and tunnels. The rooms are numbered 1,2,...,n.

Then, there are n integers k_1,k_2,...,k_n: the number of coins in each room.

Finally, there are m lines describing the tunnels. Each line has two integers a and b: there is a tunnel from room a to room b. Each tunnel is a one-way tunnel.

Output

Print one integer: the maximum number of coins you can collect.

Constraints

1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= k_i <= 10^9
1 <= a,b <= n

Example

Input:
4 4
4 5 2 7
1 2
2 1
1 3
2 4

Output:
16 
'''