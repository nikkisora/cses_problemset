'''

CSES - Shortest Routes I



Time limit: 1.00 s
Memory limit: 512 MB

There are n cities and m flight connections between them. Your task is to determine the length of the shortest route from Syrj�l� to every city.

Input

The first input line has two integers n and m: the number of cities and flight connections. The cities are numbered 1,2,...,n, and city 1 is Syrj�l�.

After that, there are m lines describing the flight connections. Each line has three integers a, b and c: a flight begins at city a, ends at city b, and its length is c. Each flight is a one-way flight.

You can assume that it is possible to travel from Syrj�l� to all other cities.

Output

Print n integers: the shortest route lengths from Syrj�l� to cities 1,2,...,n.

Constraints

1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= a,b <= n
1 <= c <= 10^9

Example

Input:
3 4
1 2 6
1 3 2
3 2 3
1 3 4

Output:
0 5 2 
'''