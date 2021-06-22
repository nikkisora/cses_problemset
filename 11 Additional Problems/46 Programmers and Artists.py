'''

CSES - Programmers and Artists



Time limit: 1.00 s
Memory limit: 512 MB

A company wants to hire a programmers and b artists.

There are a total of n applicants, and each applicant can become either a programmer or an artist. You know each applicant's programming and artistic skills.

Your task is to select the new employees so that the sum of their skills is maximum.

Input

The first input line has three integers a, b and n: the required number of programmers and artists, and the total number of applicants.

After this, there are n lines that describe the applicants. Each line has two integers x and y: the applicant's programming and artistic skills.

Output

Print one integer: the maximum sum of skills.

Constraints

 1 <= n <= 2 * 10^5
 0 <= a,b <= n
 a+b <= n
 1 <= x,y <= 10^9

Example

Input:
2 1 4
3 7
9 8
1 5
4 2

Output:
20

Explanation: An optimal solution is to hire two programmers with skills 9 and 4 and one artist with skill 7. The sum of the skills is 9+4+7=20.    
'''