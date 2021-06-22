'''

CSES - Cyclic Array



Time limit: 1.00 s
Memory limit: 512 MB

You are given a cyclic array consisting of n values. Each element has two neighbors; the elements at positions n and 1 are also considered neighbors.

Your task is to divide the array into subarrays so that the sum of each subarray is at most k. What is the minimum number of subarrays?

Input

The first input line contains integers n and k.

The next line has n integers x_1,x_2,...,x_n: the contents of the array.

There is always at least one division (i.e., no value in the array is larger than k).

Output

Print one integer: the minimum number of subarrays.

Constraints

 1 <= n <= 2 * 10^5
 1 <= x_i <= 10^9
 1 <= k <= 10^{18}

Example

Input:
8 5
2 2 2 1 3 1 2 1

Output:
3

Explanation: We can create three subarrays: [2,2,1], [3,1], and [2,1,2] (remember that the array is cyclic).    
'''