'''

CSES - Visiting Cities



Time limit: 1.00 s
Memory limit: 512 MB

You want to travel from Syrj�l� to Lehm�l� by plane using a minimum-price route. Which cities will you certainly visit?

Input

The first input line contains two integers n and m: the number of cities and the number of flights. The cities are numbered 1,2,...,n. City 1 is Syrj�l�, and city n is Lehm�l�.

After this, there are m lines describing the flights. Each line has three integers a, b, and c: there is a flight from city a to city b with price c. All flights are one-way flights.

You may assume that there is a route from Syrj�l� to Lehm�l�.

Output

First print an integer k: the number of cities that are certainly in the route. After this, print the k cities sorted in increasing order.

Constraints

1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= a,b <= n
1 <= c <= 10^9

Example

Input:
5 6
1 2 3
1 3 4
2 3 1
2 4 5
3 4 1
4 5 8

Output:
4
1 3 4 5 
'''