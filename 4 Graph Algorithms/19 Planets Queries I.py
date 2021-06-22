'''

CSES - Planets Queries I



Time limit: 1.00 s
Memory limit: 512 MB

You are playing a game consisting of n planets. Each planet has a teleporter to another planet (or the planet itself).

Your task is to process q queries of the form: when you begin on planet x and travel through k teleporters, which planet will you reach?

Input

The first input line has two integers n and q: the number of planets and queries. The planets are numbered 1,2,...,n.

The second line has n integers t_1,t_2,...,t_n: for each planet, the destination of the teleporter. It is possible that t_i=i.

Finally, there are q lines describing the queries. Each line has two integers x and k: you start on planet x and travel through k teleporters.

Output

Print the answer to each query.

Constraints

1 <= n, q <= 2 * 10^5
1 <= t_i <= n
1 <= x <= n
0 <= k <= 10^9

Example

Input:
4 3
2 1 1 4
1 2
3 4
4 1

Output:
1
2
4 
'''