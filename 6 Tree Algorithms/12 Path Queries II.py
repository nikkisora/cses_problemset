'''

CSES - Path Queries II



Time limit: 1.00 s
Memory limit: 512 MB

You are given a tree consisting of n nodes. The nodes are numbered 1,2,...,n. Each node has a value.

Your task is to process following types of queries:
 change the value of node s to x
 find the maximum value on the path between nodes a and b.

Input

The first input line contains two integers n and q: the number of nodes and queries. The nodes are numbered 1,2,...,n.

The next line has n integers v_1,v_2,...,v_n: the value of each node.

Then there are n-1 lines describing the edges. Each line contains two integers a and b: there is an edge between nodes a and b.

Finally, there are q lines describing the queries. Each query is either of the form "1 s x" or "2 a b".

Output

Print the answer to each query of type 2.

Constraints

1 <= n, q <= 2 * 10^5
1 <= a,b, s <= n
1 <= v_i, x <= 10^9

Example

Input:
5 3
2 4 1 3 3
1 2
1 3
2 4
2 5
2 3 5
1 2 2
2 3 5

Output:
4 3 
'''