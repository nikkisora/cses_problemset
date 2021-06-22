'''

CSES - Monster Game II



Time limit: 1.00 s
Memory limit: 512 MB

You are playing a game that consists of n levels. Each level has a monster. On levels 1,2,...,n-1, you can either kill or escape the monster. However, on level n you must kill the final monster to win the game.

Killing a monster takes sf time where s is the monster's strength and f is your skill factor. After killing a monster, you get a new skill factor  (lower skill factor is better). What is the minimum total time in which you can win the game?

Input

The first input line has two integers n and x: the number of levels and your initial skill factor.

The second line has n integers s_1,s_2,...,s_n: each monster's strength.

The third line has n integers f_1,f_2,...,f_n: your new skill factor after killing a monster.

Output

Print one integer: the minimum total time to win the game.

Constraints

 1 <= n <= 2 * 10^5
 1 <= x <= 10^6
 1 <= s_i, f_i <= 10^6

Example

Input:
5 100
50 20 30 90 30
60 20 20 10 90

Output:
2600

Explanation: The best way to play is to kill the second and fifth monster.    
'''