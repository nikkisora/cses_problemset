'''

CSES - Necessary Cities



Time limit: 1.00 s
Memory limit: 512 MB

There are n cities and m roads between them. There is a route between any two cities.

A city is called necessary if there is no route between some other two cities after removing that city (and adjacent roads). Your task is to find all necessary cities.

Input

The first input line has two integers n and m: the number of cities and roads. The cities are numbered 1,2,...,n.

After this, there are m lines that describe the roads. Each line has two integers a and b: there is a road between cities a and b. There is at most one road between two cities, and every road connects two distinct cities.

Output

First print an integer k: the number of necessary cities. After that, print a list of k cities. You may print the cities in any order.

Constraints

2 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= a,b <= n

Example

Input:
5 5
1 2
1 4
2 4
3 5
4 5

Output:
2
4 5 
'''