'''

CSES - Book Shop II



Time limit: 1.00 s
Memory limit: 512 MB

You are in a book shop which sells n different books. You know the price, the number of pages and the number of copies of each book.

You have decided that the total price of your purchases will be at most x. What is the maximum number of pages you can buy? You can buy several copies of the same book.

Input

The first input line contains two integers n and x: the number of book and the maximum total price.

The next line contains n integers h_1,h_2,...,h_n: the price of each book.

The next line contains n integers s_1,s_2,...,s_n: the number of pages of each book.

The last line contains n integers k_1,k_2,...,k_n: the number of copies of each book.

Output

Print one integer: the maximum number of pages.

Constraints

1 <= n <= 100
1 <= x <= 10^5
1 <= h_i, s_i, k_i <= 1000

Example

Input:
3 10
2 6 3
8 5 4
3 5 2

Output:
28

Explanation: You can buy three copies of book 1 and one copy of book 3. The price is 3 * 2 + 3 = 9 and the number of pages is 3 * 8 + 4 = 28.    
'''