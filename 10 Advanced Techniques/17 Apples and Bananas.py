'''

CSES - Apples and Bananas



Time limit: 1.00 s
Memory limit: 512 MB

There are apples and bananas and each of them has an integer weight between 1 ... k. Your task is to calculate for each weight w between 2...2k the number of ways we can choose an apple and a banana whose combined weight is w.

Input

The first input line contains three integers k, n and m: the number k, the number of apples and the number of bananas.

The next line contains n integers a_1,a_2,...,a_n: weight of each apple.

The last line contains m integers b_1,b_2,...,b_m: weight of each banana.

Output

For each integer w between 2 ... 2k print the number of ways to choose an apple and a banana whose combined weight is w.

Constraints

1 <= k,n,m <= 2 * 10^5
1 <= a_i <= k
1 <= b_i <= k

Example

Input:
5 3 4
5 2 5
4 3 2 3

Output:
0 0 1 2 1 2 4 2 0  

Explanation: For example for w = 8 there are 4 different ways: we can pick an apple of weight 5 in two different ways and a banana of weight 3 in two different ways.    
'''