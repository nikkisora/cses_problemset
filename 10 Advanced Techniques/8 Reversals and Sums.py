'''

CSES - Reversals and Sums



Time limit: 1.00 s
Memory limit: 512 MB

Given an array of n integers, you have to process following operations:

 reverse a subarray
 calculate the sum of values in a subarray

Input

The first input line has two integers n and m: the size of the array and the number of operations. The array elements are numbered 1,2,...,n.

The next line as n integers x_1,x_2,...,x_n: the contents of the array.

Finally, there are m lines that describe the operations. Each line has three integers t, a and b. If t=1, you should reverse a subarray from a to b. If t=2, you should calculate the sum of values from a to b.

Output

Print the answer to each operation where t=2.

Constraints

 1 <= n <= 2 * 10^5
 1 <= m <= 10^5
 0 <= x_i <= 10^9
 1 <= a <= b <= n

Example

Input:
8 3
2 1 3 4 5 3 4 4
2 2 4
1 3 6
2 2 4

Output:
8
9 
'''