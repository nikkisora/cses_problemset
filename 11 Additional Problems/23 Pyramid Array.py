'''

CSES - Pyramid Array



Time limit: 1.00 s
Memory limit: 512 MB

You are given an array consisting of n distinct integers. On each move, you can swap any two adjacent values.

You want to transform the array into a pyramid array. This means that the final array has to be first increasing and then decreasing. It is also allowed that the final array is only increasing or decreasing.

What is the minimum number of moves needed?

Input

The first input line has an integer n: the size of the array.

The next line has n distinct integers x_1,x_2,...,x_n: the contents of the array.

Output

Print one integer: the minimum number of moves.

Constraints

1 <= n <= 2 * 10^5
1 <= x_i <= 10^9

Example

Input:
4
2 1 5 3

Output:
1

Explanation: You may swap the first two values which creates a pyramid array [1,2,5,3].    
'''