'''

CSES - Hamiltonian Flights



Time limit: 1.00 s
Memory limit: 512 MB

There are n cities and m flight connections between them. You want to travel from Syrj�l� to Lehm�l� so that you visit each city exactly once. How many possible routes are there?

Input

The first input line has two integers n and m: the number of cities and flights. The cities are numbered 1,2,...,n. City 1 is Syrj�l�, and city n is Lehm�l�.

Then, there are m lines describing the flights. Each line has two integers a and b: there is a flight from city a to city b. All flights are one-way flights.

Output

Print one integer: the number of routes modulo 10^9+7.

Constraints

2 <= n <= 20
1 <= m <= n^2
1 <= a,b <= n

Example

Input:
4 6
1 2
1 3
2 3
3 2
2 4
3 4

Output:
2 
'''