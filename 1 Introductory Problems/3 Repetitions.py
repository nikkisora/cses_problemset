'''

CSES - Repetitions



Time limit: 1.00 s
Memory limit: 512 MB

You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.

Input


The only input line contains a string of n characters.

Output


Print one integer: the length of the longest repetition.

Constraints

1 <= n <= 10^6

Example


Input:
ATTCGGGA


Output:
3 
'''

s = input()
max_rep = 0
rep = 1
for p, c in zip(s, s[1:]):
    if p != c:
        if rep > max_rep:
            max_rep = rep
        rep = 1
    else:
        rep+=1

print(max(max_rep, rep))