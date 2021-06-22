'''

CSES - Strongly Connected Edges



Time limit: 1.00 s
Memory limit: 512 MB

Given an undirected graph, your task is to choose a direction for each edge so that the resulting directed graph is strongly connected.

Input

The first input line has two integers n and m: the number of nodes and edges. The nodes are numbered 1,2,...,n.

After this, there are m lines describing the edges. Each line has two integers a and b: there is an edge between nodes a and b.

You may assume that the graph is simple, i.e., there are at most one edge between two nodes and every edge connects two distinct nodes.

Output

Print m lines describing the directions of the edges. Each line has two integers a and b: there is an edge from node a to node b. You can print any valid solution.

If there are no solutions, only print "IMPOSSIBLE".

Constraints

1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= a,b <= n

Example

Input:
3 3
1 2
1 3
2 3

Output:
1 2
2 3
3 1 
'''