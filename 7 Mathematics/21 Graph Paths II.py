'''

CSES - Graph Paths II



Time limit: 1.00 s
Memory limit: 512 MB

Consider a directed weighted graph having n nodes and m edges. Your task is to calculate the minimum path length from node 1 to node n with exactly k edges.

Input

The first input line contains three integers n, m and k: the number of nodes and edges, and the length of the path. The nodes are numbered 1,2,...,n.

Then, there are m lines describing the edges. Each line contains three integers a, b and c: there is an edge from node a to node b with weight c.

Output

Print the minimum path length. If there are no such paths, print -1.

Constraints

1 <= n <= 100
1 <= m <= n(n-1)
1 <= k <= 10^9
1 <= a,b <= n
1 <= c <= 10^9

Example

Input:
3 4 8
1 2 5
2 3 4
3 1 1
3 2 2

Output:
27 
'''