'''

CSES - Range Updates and Sums



Time limit: 1.00 s
Memory limit: 512 MB

Your task is to maintain an array of n values and efficiently process the following types of queries:
 Increase each value in range [a,b] by x.
 Set each value in range [a,b] to x.
 Calculate the sum of values in range [a,b].

Input

The first input line has two integers n and q: the array size and the number of queries.

The next line has n values t_1,t_2,...,t_n: the initial contents of the array.

Finally, there are q lines describing the queries. The format of each line is one of the following: "1 a b x",  "2 a b x", or "3 a b". 

Output

Print the answer to each sum query.

Constraints

 1 <= n, q <= 2 * 10^5
 1 <= t_i, x <= 10^6
 1 <= a <= b <= n

Example

Input:
6 5
2 3 1 1 5 3
3 3 5
1 2 4 2
3 3 5
2 2 4 5
3 3 5

Output:
7
11
15 
'''