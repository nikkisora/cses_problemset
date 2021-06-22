'''

CSES - Graph Girth



Time limit: 1.00 s
Memory limit: 512 MB

Given an undirected graph, your task is to determine its girth, i.e., the length of its shortest cycle.

Input

The first input line has two integers n and m: the number of nodes and edges. The nodes are numbered 1,2,...,n.

After this, there are m lines describing the edges. Each line has two integers a and b: there is an edge between nodes a and b.

You may assume that there is at most one edge between each two nodes.

Output

Print one integer: the girth of the graph. If there are no cycles, print -1.

Constraints

1 <= n <= 2500
1 <= m <= 5000

Example

Input:
5 6
1 2
1 3
2 4
2 5
3 4
4 5

Output:
3 
'''