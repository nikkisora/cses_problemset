'''

CSES - Network Breakdown



Time limit: 1.00 s
Memory limit: 512 MB

Syrj�l�'s network has n computers and m connections between them. The network consists of components of computers that can send messages to each other.

Nobody in Syrj�l� understands how the network works. For this reason, if a connection breaks down, nobody will repair it. In this situation a component may be divided into two components.

Your task is to calculate the number of components after each connection breakdown.

Input

The first input line has three integers n, m and k: the number of computers, connections and breakdowns. The computers are numbered 1,2,...,n.

Then, there are m lines describing the connections. Each line has two integers a and b: there is a connection between computers a and b. Each connection is between two different computers, and there is at most one connection between two computers.

Finally, there are k lines describing the breakdowns. Each line has two integers a and b: the connection between computers a and b breaks down.

Output

After each breakdown, print the number of components.

Constraints

1 <= n <= 10^5
1 <= m <= 2 * 10^5
1 <= k <= m
1 <= a,b <= n

Example

Input:
5 5 3
1 2
1 3
2 3
3 4
4 5
3 4
2 3
4 5

Output:
2 2 3 
'''