'''

CSES - New Flight Routes



Time limit: 1.00 s
Memory limit: 512 MB

There are n cities and m flight connections between them. Your task is to add new flights so that it will be possible to travel from any city to any other city. What is the minimum number of new flights required?

Input

The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,...,n.

After this, there are m lines describing the flights. Each line has two integers a and b: there is a flight from city a to city b. All flights are one-way flights.

Output

First print an integer k: the required number of new flights. After this, print k lines describing the new flights. You can print any valid solution.

Constraints

1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= a,b <= n

Example

Input:
4 5
1 2
2 3
3 1
1 4
3 4

Output:
1
4 2 
'''