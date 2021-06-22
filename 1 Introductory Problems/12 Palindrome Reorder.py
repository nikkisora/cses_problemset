'''

CSES - Palindrome Reorder



Time limit: 1.00 s
Memory limit: 512 MB

Given a string, your task is to reorder its letters in such a way that it becomes a palindrome (i.e., it reads the same forwards and backwards).

Input


The only input line has a string of length n consisting of characters A�Z.

Output


Print a palindrome consisting of the characters of the original string. You may print any valid solution. If there are no solutions, print "NO SOLUTION".

Constraints

1 <= n <= 10^6

Example


Input:
AAAACACBA


Output:
AACABACAA 
'''
from collections import Counter

def main():
    s = input()

    counter = Counter(s)
    ans = ''
    odd = ''
    for char, num in counter.items():
        if num%2==0:
            ans += char*(num//2)
            
        elif num%2 and not odd:
            if len(s)%2==0:
                print('NO SOLUTION')
                return
            odd = char
            
        else:
            print('NO SOLUTION')
            return
        
    if not odd and len(s)%2:
        print('NO SOLUTION')
        return
    print(ans + odd*counter[odd] + ans[::-1])
        
main()
