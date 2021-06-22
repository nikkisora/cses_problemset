'''

CSES - Creating Strings



Time limit: 1.00 s
Memory limit: 512 MB

Given a string, your task is to generate all different strings that can be created using its characters.

Input


The only input line has a string of length n. Each character is between a�z.

Output


First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.

Constraints

1 <= n <= 8

Example


Input:
aabac


Output:
20

aaabc

aaacb

aabac

aabca

aacab

aacba

abaac

abaca

abcaa

acaab

acaba

acbaa

baaac

baaca

bacaa

bcaaa

caaab

caaba

cabaa

cbaaa 
'''

from itertools import permutations

n = input()

combinations = sorted(set(permutations(n, len(n))))

print(len(combinations))
for comb in combinations:
    print(''.join(comb))