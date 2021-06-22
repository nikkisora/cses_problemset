'''

CSES - Edit Distance



Time limit: 1.00 s
Memory limit: 512 MB

The edit distance between two strings is the minimum number of operations required to transform one string into the other.

The allowed operations are:
Add one character to the string.
Remove one character from the string.
Replace one character in the string.

For example, the edit distance between LOVE and MOVIE is 2, because you can first replace L with M, and then add I.

Your task is to calculate the edit distance between two strings.

Input

The first input line has a string that contains n characters between A�Z.

The second input line has a string that contains m characters between A�Z.

Output

Print one integer: the edit distance between the strings.

Constraints

1 <= n,m <= 5000

Example

Input:
LOVE
MOVIE

Output:
2 
'''