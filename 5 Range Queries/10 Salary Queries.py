'''

CSES - Salary Queries



Time limit: 1.00 s
Memory limit: 512 MB

A company has n employees with certain salaries. Your task is to keep track of the salaries and process queries.

Input

The first input line contains two integers n and q: the number of employees and queries. The employees are numbered 1,2,...,n.

The next line has n integers p_1,p_2,...,p_n: each employee's salary.

After this, there are q lines describing the queries. Each line has one of the following forms:
! k x: change the salary of employee k to x
? a b: count the number of employees whose salary is between a ... b

Output

Print the answer to each ? query.

Constraints

1 <= n, q <= 2 * 10^5
1 <= p_i <= 10^9
1 <= k <= n
1 <= x <= 10^9
1 <= a <= b <= 10^9

Example

Input:
5 3
3 7 2 2 5
? 2 3
! 3 6
? 2 3

Output:
3
2 
'''