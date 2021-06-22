'''

CSES - Critical Cities



Time limit: 1.00 s
Memory limit: 512 MB

There are n cities and m flight connections between them. A city is called a critical city if it appears on every route from a city to another city.

Your task is to find all critical cities from Syrj�l� to Lehm�l�.

Input

The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,...,n. City 1 is Syrj�l�, and city n is Lehm�l�.

Then, there are m lines describing the roads. Each line has two integers a and b: there is a flight from city a to city b. All flights are one-way flights.

You may assume that there is a route from Syrj�l� to Lehm�l�.

Output

First print an integer k: the number of critical cities. After this, print k integers: the critical cities in increasing order.

Constraints

2 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= a,b <= n

Example

Input:
5 5
1 2
2 3
2 4
3 5
4 5

Output:
3
1 2 5 
'''