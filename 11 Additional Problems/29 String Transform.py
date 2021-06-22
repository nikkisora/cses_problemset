'''

CSES - String Transform



Time limit: 1.00 s
Memory limit: 512 MB

Consider the following string transformation:

 append the character # to the string (we assume that # is lexicographically smaller than all other characters of the string)
 generate all rotations of the string
 sort the rotations in increasing order
 based on this order, construct a new string that contains the last character of each rotation

For example, the string babc becomes babc#. Then, the sorted list of rotations is #babc, abc#b, babc#, bc#ba, and c#bab. This yields a string cb#ab.

Input

The only input line contains the transformed string of length n+1. Each character of the original string is one of a�z.

Output

Print the original string of length n.

Constraints

1 <= n <= 10^6

Example

Input:
cb#ab

Output:
babc 
'''