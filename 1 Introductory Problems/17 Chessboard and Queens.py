'''

CSES - Chessboard and Queens



Time limit: 1.00 s
Memory limit: 512 MB

Your task is to place eight queens on a chessboard so that no two queens are attacking each other. As an additional challenge, each square is either free or reserved, and you can only place queens on the free squares. However, the reserved squares do not prevent queens from attacking each other.


How many possible ways are there to place the queens?

Input


The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).

Output


Print one integer: the number of ways you can place the queens.

Example


Input:
........
........
..*.....
........
........
.....**.
...*....
........


Output:
65 
'''

n = 8
board = []
for _ in range(n):
    row = input()
    board.append([])
    for i, cell in enumerate((row)):
        if cell == '*':
            board[-1].append(i)

ans = 0

def place(row, vert, ldiag, rdiag):
    if row == n:
        global ans
        ans += 1
    else:
        for col in range(n):
            if col in board[row]:continue
            vmask, lmask, rmask = 1 << col, 1 << (row+col), 1 << (n-row-1+col)
            if vert & vmask or ldiag & lmask or rdiag & rmask: continue
            place(row+1, vert | vmask, ldiag | lmask, rdiag | rmask)

place(0, 0, 0, 0)
print(ans)