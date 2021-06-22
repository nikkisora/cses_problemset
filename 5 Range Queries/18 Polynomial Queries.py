'''

CSES - Polynomial Queries



Time limit: 1.00 s
Memory limit: 512 MB

Your task is to maintain an array of n values and efficiently process the following types of queries:
Increase the first value in range [a,b] by 1, the second value by 2, the third value by 3, and so on.
Calculate the sum of values in range [a,b].

Input

The first input line has two integers n and q: the size of the array and the number of queries.

The next line has n values t_1,t_2,...,t_n: the initial contents of the array.

Finally, there are q lines describing the queries. The format of each line is either "1 a b" or "2 a b".

Output

Print the answer to each sum query.

Constraints

 1 <= n, q <= 2 * 10^5
 1 <= t_i <= 10^6
 1 <= a <= b <= n

Example

Input:
5 3
4 2 3 1 7
2 1 5
1 1 5
2 1 5

Output:
17
32 
'''