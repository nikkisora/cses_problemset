'''

CSES - Subarray Sum Queries



Time limit: 1.00 s
Memory limit: 512 MB

There is an array consisting of n integers. Some values of the array will be updated, and after each update, your task is to report the maximum subarray sum in the array. 

Input

The first input line contains integers n and m: the size of the array and the number of updates. The array is indexed 1,2,...,n.

The next line has n integers: x_1,x_2,...,x_n: the initial contents of the array.

Then there are m lines describing the changes. Each line has two integers k and x: the value at position k becomes x.

Output

After each update, print the maximum subarray sum. Empty subarrays (with sum 0) are allowed.

Constraints

1 <= n, m <= 2 * 10^5
-10^9 <= x_i <= 10^9
1 <= k <= n
-10^9 <= x <= 10^9

Example

Input:
5 3
1 2 -3 5 -1
2 6
3 1
2 -2

Output:
9
13
6 
'''