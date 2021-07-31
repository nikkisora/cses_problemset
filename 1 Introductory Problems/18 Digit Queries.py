'''

CSES - Digit Queries



Time limit: 1.00 s
Memory limit: 512 MB

Consider an infinite string that consists of all positive integers in increasing order:

12345678910111213141516171819202122232425...


Your task is to process q queries of the form: what is the digit at position k in the string?

Input


The first input line has an integer q: the number of queries.


After this, there are q lines that describe the queries. Each line has an integer k: a 1-indexed position in the string.

Output


For each query, print the corresponding digit.

Constraints

 1 <= q <= 1000
 1 <= k <= 10^{18}

Example


Input:
3
7
19
12


Output:
7

4

1 
'''

from math import ceil

n = int(input())

queries = []
for _ in range(n):
    queries.append(int(input()))
    
brut_string = ''
for i in range(1, 300):
    brut_string += str(i)

for q in queries:
    sum = 0
    x = 0
    
    while sum < q:
        sum += 9 * 10**x * (x+1)
        x+=1
    sum -= 9 * 10**(x-1) * x
    
    difference = q - sum
    landing_number = ceil(10**(x-1) + difference//x - 1)
    if difference % x:
        landing_number += 1
    landing_digit = difference % x - 1
        
    print(str(landing_number)[landing_digit])
    
    