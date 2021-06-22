'''

CSES - Knuth Division



Time limit: 1.00 s
Memory limit: 512 MB

Given an array of n numbers, your task is to divide it into n subarrays, each of which has a single element.

On each move, you may choose any subarray and split it into two subarrays. The cost of such a move is the sum of values in the chosen subarray.

What is the minimum total cost if you act optimally?

Input

The first input line has an integer n: the array size. The array elements are numbered 1,2,...,n.

The second line has n integers x_1,x_2,...,x_n: the contents of the array.

Output

Print one integer: the minimum total cost.

Constraints

1 <= n <= 5000
1 <= x_i <= 10^9

Example

Input:
5
2 7 3 2 5

Output:
43 
'''