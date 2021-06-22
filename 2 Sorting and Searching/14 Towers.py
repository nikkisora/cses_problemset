'''

CSES - Towers



Time limit: 1.00 s
Memory limit: 512 MB

You are given n cubes in a certain order, and your task is to build towers using them. Whenever two cubes are one on top of the other, the upper cube must be smaller than the lower cube.

You must process the cubes in the given order. You can always either place the cube on top of an existing tower, or begin a new tower. What is the minimum possible number of towers?

Input

The first input line contains an integer n: the number of cubes.

The next line contains n integers k_1,k_2,...,k_n: the sizes of the cubes.

Output

Print one integer: the minimum number of towers.

Constraints

1 <= n <= 2 * 10^5
1 <= k_i <= 10^9

Example

Input:
5
3 8 2 1 5

Output:
2 
'''