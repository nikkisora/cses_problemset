'''

CSES - Inversion Probability



Time limit: 1.00 s
Memory limit: 512 MB

An array has n integers x_1,x_2,...,x_n, and each of them has been randomly chosen between 1 and r_i. An inversion is a pair (a,b) where a<b and x_a>x_b.

What is the expected number of inversions in the array?

Input

The first input line contains an integer n: the size of the array.

The second line contains n integers r_1,r_2,...,r_n: the range of possible values for each array position.

Output

Print the expected number of inversions rounded to six decimal places.

Constraints

1 <= n <= 100
1 <= r_i <= 100

Example

Input:
3
5 2 7

Output:
1.057143 
'''