'''

CSES - Intersection Points



Time limit: 1.00 s
Memory limit: 512 MB

Given n horizontal and vertical line segments, your task is to calculate the number of their intersection points.

You may assume that no parallel line segments overlap, and no two line segments have a common endpoint.

Input

The first input line has an integer n: the number of line segments.

Then there are n lines describing the line segments. Each line has four integers: x_1, y_1, x_2 and y_2: a line segment begins at point (x_1,y_1) and ends at point (x_2,y_2).

Output

Print the number of intersection points.

Constraints

1 <= n <= 10^5
-10^6 <= x_1 <= x_2 <= 10^6
-10^6 <= y_1 <= y_2 <= 10^6

Example

Input:
3
2 3 7 3
3 1 3 5
6 2 6 6

Output:
2 
'''