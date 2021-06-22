'''

CSES - Stick Divisions



Time limit: 1.00 s
Memory limit: 512 MB

You have a stick of length x and you want to divide it into n sticks, with given lengths, whose total length is x.

On each move you can take any stick and divide it into two sticks. The cost of such an operation is the length of the original stick.

What is the minimum cost needed to create the sticks?

Input

The first input line has two integers x and n: the length of the stick and the number of sticks in the division.

The second line has n integers d_1,d_2,...,d_n: the length of each stick in the division.

Output

Print one integer: the minimum cost of the division.

Constraints

1 <= x <= 10^9
1 <= n <= 2 * 10^5
\sum d_i = x

Example

Input:
8 3
2 3 3

Output:
13

Explanation: You first divide the stick of length 8 into sticks of length 3 and 5 (cost 8). After this, you divide the stick of length 5 into sticks of length 2 and 3 (cost 5). The total cost is 8+5=13.    
'''