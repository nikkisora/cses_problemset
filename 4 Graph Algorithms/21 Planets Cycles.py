'''

CSES - Planets Cycles



Time limit: 1.00 s
Memory limit: 512 MB

You are playing a game consisting of n planets. Each planet has a teleporter to another planet (or the planet itself).

You start on a planet and then travel through teleporters until you reach a planet that you have already visited before.

Your task is to calculate for each planet the number of teleportations there would be if you started on that planet.

Input

The first input line has an integer n: the number of planets. The planets are numbered 1,2,...,n.

The second line has n integers t_1,t_2,...,t_n: for each planet, the destination of the teleporter. It is possible that t_i=i.

Output

Print n integers according to the problem statement.

Constraints

1 <= n <= 2 * 10^5
1 <= t_i <= n

Example

Input:
5
2 4 3 1 4

Output:
3 3 1 3 4 
'''