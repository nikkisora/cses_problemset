'''

CSES - Range Xor Queries



Time limit: 1.00 s
Memory limit: 512 MB

Given an array of n integers, your task is to process q queries of the form: what is the xor sum of values in range [a,b]?

Input

The first input line has two integers n and q: the number of values and queries.

The second line has n integers x_1,x_2,...,x_n: the array values.

Finally, there are q lines describing the queries. Each line has two integers a and b: what is the xor sum of values in range [a,b]?

Output

Print the result of each query.

Constraints

1 <= n,q <= 2 * 10^5
1 <= x_i <= 10^9
1 <= a <= b <= n

Example

Input:
8 4
3 2 4 5 1 1 5 3
2 4
5 6
1 8
3 3

Output:
3
0
6
4 
'''