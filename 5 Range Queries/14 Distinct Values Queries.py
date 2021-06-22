'''

CSES - Distinct Values Queries



Time limit: 1.00 s
Memory limit: 512 MB

You are given an array of n integers and q queries of the form: how many distinct values are there in a range [a,b]?

Input

The first input line has two integers n and q: the array size and number of queries.

The next line has n integers x_1,x_2,...,x_n: the array values.

Finally, there are q lines describing the queries. Each line has two integers a and b.

Output

For each query, print the number of distinct values in the range.

Constraints

1 <= n,q <= 2 * 10^5
1 <= x_i <= 10^9
1 <= a <= b <= n

Example

Input:
5 3
3 2 3 1 2
1 3
2 4
1 5

Output:
2
3
3 
'''